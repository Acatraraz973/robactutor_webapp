import { useEffect, useState } from "react";
import { startPractice, gradePractice } from "../api";
import MarkdownLite from "./MarkdownLite";
import ReferencePassages from "./ReferencePassages";

// idle -> loadingQuestion -> question -> grading -> result
export default function PracticeScreen({ t, subject, sessionId, onAnswered }) {
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
    if (!answer.trim() || phase === "grading") return;
    setPhase("grading");
    setError(null);
    try {
      const graded = await gradePractice(sessionId, question.question_id, answer.trim());
      setResult(graded);
      setPhase("result");
      onAnswered?.();
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
          <h1 className="screen-title">{t.practiceTitle}</h1>
          <p className="screen-intro">{t.practiceIntro}</p>

          {error && <div className="screen-error">{error}</div>}

          {phase === "idle" && (
            <button type="button" className="primary-btn" onClick={loadQuestion}>
              {t.practiceStartButton}
            </button>
          )}

          {phase === "loadingQuestion" && (
            <div className="screen-loading">
              <span className="typing-dots"><span></span><span></span><span></span></span>
              <span>{t.practiceLoadingQuestion}</span>
            </div>
          )}

          {(phase === "question" || phase === "grading") && question && (
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
                  placeholder={t.practiceAnswerPlaceholder}
                  disabled={phase === "grading"}
                  rows={7}
                />
                <button type="submit" className="primary-btn" disabled={phase === "grading" || !answer.trim()}>
                  {phase === "grading" ? t.practiceGrading : t.practiceSubmitButton}
                </button>
              </form>
            </>
          )}

          {phase === "result" && result && (
            <div className="result-card">
              <div className="score-row">
                <div className="score-block">
                  <div className="score-number">
                    <span className="score-value">{result.punctaj_estimat}</span>
                    <span className="score-total">/ {result.punctaj_total}</span>
                  </div>
                  <span className="score-label">{t.practiceScoreLabel}</span>
                </div>
                <div className="score-block score-block-secondary">
                  <span className="score-value-sm">{Math.round(result.similaritate * 100)}%</span>
                  <span className="score-label">{t.practiceSimilarityLabel}</span>
                </div>
              </div>

              {result.raspuns_final_potrivit !== null && (
                <span className={"final-answer-badge " + (result.raspuns_final_potrivit ? "is-correct" : "is-incorrect")}>
                  {result.raspuns_final_potrivit ? "✓" : "✕"}{" "}
                  {result.raspuns_final_potrivit ? t.finalAnswerCorrect : t.finalAnswerIncorrect}
                </span>
              )}

              <div className="result-section">
                <h2 className="result-section-label">{t.practiceBaremLabel}</h2>
                <div className="barem-card">
                  <MarkdownLite text={result.barem_oficial} />
                </div>
              </div>

              <ReferencePassages t={t} label={t.practiceReferenceLabel} passages={result.material_referinta} />

              <button type="button" className="primary-btn" onClick={loadQuestion}>
                {t.practiceNextButton}
              </button>
            </div>
          )}
        </div>
      </div>
    </main>
  );
}
