export default function ReferencePassages({ t, label, passages }) {
  if (!passages || passages.length === 0) return null;
  return (
    <div className="result-section">
      <h2 className="result-section-label">{label}</h2>
      <div className="msg-sources">
        {passages.map((s, i) => (
          <div className="source-chip" key={i}>
            <div className="source-chip-meta">
              <span className="source-label">{t.sourceLabel}:</span>
              <span className="source-file">{s.filename || "—"}</span>
              <span className="source-score">
                {typeof s.score === "number" ? s.score.toFixed(2) : ""}
              </span>
            </div>
            {s.text && <p className="source-excerpt">{s.text}</p>}
          </div>
        ))}
      </div>
    </div>
  );
}
