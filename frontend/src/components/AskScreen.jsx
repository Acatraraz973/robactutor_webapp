import { useEffect, useRef, useState } from "react";
import { askQuestion } from "../api";
import MarkdownLite from "./MarkdownLite";
import ReferencePassages from "./ReferencePassages";

export default function AskScreen({ t, subject, onAsked }) {
  const [question, setQuestion] = useState("");
  const [isAsking, setIsAsking] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);
  const inputRef = useRef(null);

  useEffect(() => {
    setResult(null);
    setError(null);
    inputRef.current?.focus();
  }, [subject]);

  async function handleSubmit(e) {
    e.preventDefault();
    const trimmed = question.trim();
    if (!trimmed || isAsking) return;
    setIsAsking(true);
    setError(null);
    try {
      const data = await askQuestion(subject, trimmed);
      setResult(data);
      onAsked?.();
    } catch (err) {
      console.error(err);
      setError(t.errorMessage);
    } finally {
      setIsAsking(false);
      inputRef.current?.focus();
    }
  }

  return (
    <main className="screen">
      <div className="screen-scroll">
        <div className="screen-inner">
          <h1 className="screen-title">{t.askTitle}</h1>
          <p className="screen-intro">{t.askIntro}</p>

          <form onSubmit={handleSubmit} className="answer-form">
            <input
              ref={inputRef}
              type="text"
              className="composer-input"
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
              placeholder={t.askPlaceholder}
              disabled={isAsking}
              autoComplete="off"
            />
            <button type="submit" className="primary-btn" disabled={isAsking || !question.trim()}>
              {t.askSubmitButton}
            </button>
          </form>

          {error && <div className="screen-error">{error}</div>}

          {isAsking && (
            <div className="screen-loading">
              <span className="typing-dots"><span></span><span></span><span></span></span>
              <span>{t.generatingLabel}</span>
            </div>
          )}

          {result && !isAsking && (
            <div className="result-card">
              <span className="experimental-badge">{t.askExperimentalBadge}</span>
              <h2 className="result-section-label">{t.askAnswerLabel}</h2>
              <div className="barem-card">
                <MarkdownLite text={result.answer} />
              </div>
              <ReferencePassages t={t} label={t.practiceReferenceLabel} passages={result.material_referinta} />
            </div>
          )}
        </div>
      </div>
    </main>
  );
}
