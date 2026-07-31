import { useEffect, useState } from "react";
import { startPractice, demoGradeComparison } from "../api";
import MarkdownLite from "./MarkdownLite";

// idle -> loadingQuestion -> question -> comparing -> result
export default function DemoScreen({ t, subject, sessionId }) {
  const [phase, setPhase] = useState("idle");
  const [question, setQuestion] = useState(null);
  const [answer, setAnswer] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    setPhase("idle");
    setQuestion(null);
    setAnswer("");
    setResult(null);
    setError(null);
  }, [subject]);

  async function loadQuestion() {
    setPhase("loadingQuestion");
    setError(null);
    try {
      const q = await startPractice(subject, sessionId);
      setQuestion(q);
      setAnswer("");
      setResult(null);
      setPhase("question");
    } catch (err) {
      console.error(err);
      setError(t.errorMessage);
      setPhase("idle");
    }
  }

  async function handleSubmit(e) {
    e.preventDefault();
    if (!answer.trim() || phase === "comparing") return;
    setPhase("comparing");
    setError(null);
    try {
      const data = await demoGradeComparison(question.question_id, answer.trim());
      setResult(data);
      setPhase("result");
    } catch (err) {
      console.error(err);
      setError(t.errorMessage);
      setPhase("question");
    }
  }

  return (
    <main className="screen">
      <div className="screen-scroll">
        <div className="screen-inner">
          <h1 className="screen-title">{t.demoTitle}</h1>
          <p className="screen-intro">{t.demoIntro}</p>

          {error && <div className="screen-error">{error}</div>}

          {phase === "idle" && (
            <button type="button" className="primary-btn" onClick={loadQuestion}>
              {t.demoGetQuestionButton}
            </button>
          )}

          {phase === "loadingQuestion" && (
            <div className="screen-loading">
              <span className="typing-dots"><span></span><span></span><span></span></span>
              <span>{t.practiceLoadingQuestion}</span>
            </div>
          )}

          {(phase === "question" || phase === "comparing") && question && (
            <>
              <div className="question-card">
                <span className="question-points">
                  {question.points_total}{" "}{t.practicePoints}
                </span>
                <MarkdownLite text={question.instruction} />
              </div>

              <form onSubmit={handleSubmit} className="answer-form">
                <textarea
                  className="answer-textarea"
                  value={answer}
                  onChange={(e) => setAnswer(e.target.value)}
                  placeholder={t.demoAnswerPlaceholder}
                  disabled={phase === "comparing"}
                  rows={5}
                />
                <button type="submit" className="primary-btn" disabled={phase === "comparing" || !answer.trim()}>
                  {phase === "comparing" ? t.demoComparing : t.demoCompareButton}
                </button>
              </form>
            </>
          )}

          {phase === "result" && result && (
            <>
              <div className="demo-disclaimer">{result.disclaimer}</div>

              <div className="compare-grid">
                <div className="result-card compare-card compare-card-validated">
                  <h2 className="result-section-label">{t.demoValidatedLabel}</h2>
                  <div className="score-row">
                    <div className="score-block">
                      <div className="score-number">
                        <span className="score-value">{result.validated_result.punctaj_estimat}</span>
                        <span className="score-total">/ {result.validated_result.punctaj_total}</span>
                      </div>
                      <span className="score-label">{t.practiceScoreLabel}</span>
                    </div>
                  </div>
                  <div className="barem-card">
                    <MarkdownLite text={result.validated_result.barem_oficial} />
                  </div>
                </div>

                <div className="result-card compare-card compare-card-raw">
                  <h2 className="result-section-label">{t.demoAdapterLabel}</h2>
                  <div className="barem-card barem-card-raw">
                    <MarkdownLite text={result.adapter_raw_output} />
                  </div>
                </div>
              </div>

              <button type="button" className="primary-btn" onClick={loadQuestion}>
                {t.practiceNextButton}
              </button>
            </>
          )}
        </div>
      </div>
    </main>
  );
}
