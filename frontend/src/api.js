// Every call here except askQuestion() uses a relative /api/... URL. In
// development, Vite's proxy (see vite.config.js) forwards these to the
// FastAPI backend on port 8000. In production, the grading service (Cloud
// Run) serves this app directly, so /api/... is already same-origin.
// Either way, this file never needs to know which mode it's running in.
//
// askQuestion() is the one exception: ask-mode runs on a separate
// deployment (HF Spaces/ZeroGPU), which only supports Gradio's own HTTP
// API, not plain REST -- see hf_space/app.py. If VITE_ASK_API_BASE is set
// (production build), it calls that Space via Gradio's two-step
// POST-then-SSE protocol. If unset (local dev), it falls back to the
// same-origin /api/ask route that local backend/app/robactutor_backend.py
// still serves directly, unchanged.

const ASK_API_BASE = import.meta.env.VITE_ASK_API_BASE || "";

async function postJson(path, body) {
  const res = await fetch(path, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  if (!res.ok) {
    const detail = await res.json().catch(() => null);
    throw new Error(detail?.detail || `${path} failed: ${res.status}`);
  }
  return res.json();
}

export async function fetchHealth() {
  const res = await fetch("/api/health");
  if (!res.ok) throw new Error("Health check failed: " + res.status);
  return res.json();
}

export async function fetchSubjects() {
  const res = await fetch("/api/subjects");
  if (!res.ok) throw new Error("Failed to load subjects: " + res.status);
  return res.json();
}

export function startPractice(subject, sessionId) {
  return postJson("/api/practice/start", { subject, session_id: sessionId });
}

export function gradePractice(sessionId, questionId, studentAnswer) {
  return postJson("/api/practice/grade", {
    session_id: sessionId,
    question_id: questionId,
    student_answer: studentAnswer,
  });
}

// Gradio's HTTP API is two calls: POST to start the run (returns an
// event_id), then GET an SSE stream of that event_id for the result. Not a
// single request/response like the rest of this file -- see api.js's
// top-of-file note and hf_space/app.py for why.
function callGradioApi(baseUrl, apiName, data) {
  // Gradio 5.x serves its HTTP API under /gradio_api/, not top-level /call/
  // -- confirmed against the deployed hf_space/app.py Space (gradio 5.x),
  // where POST /call/<name> 404s and POST /gradio_api/call/<name> works.
  return fetch(`${baseUrl}/gradio_api/call/${apiName}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ data }),
  })
    .then((res) => {
      if (!res.ok) throw new Error(`${apiName} failed: ${res.status}`);
      return res.json();
    })
    .then(({ event_id }) => new Promise((resolve, reject) => {
      const source = new EventSource(`${baseUrl}/gradio_api/call/${apiName}/${event_id}`);
      source.addEventListener("complete", (e) => {
        source.close();
        try {
          const [result] = JSON.parse(e.data);
          resolve(result);
        } catch (err) {
          reject(err);
        }
      });
      source.addEventListener("error", () => {
        source.close();
        reject(new Error(`${apiName}: stream error`));
      });
    }));
}

export function askQuestion(subject, question) {
  if (ASK_API_BASE) {
    // hf_space/app.py: btn.click(fn=ask, inputs=[question_in, subject_in], ...)
    // -- positional order here must match that inputs array.
    return callGradioApi(ASK_API_BASE, "ask", [question, subject]);
  }
  return postJson("/api/ask", { subject, question });
}

export function demoGradeComparison(questionId, studentAnswer) {
  return postJson("/api/demo/grade-comparison", {
    question_id: questionId,
    student_answer: studentAnswer,
  });
}
