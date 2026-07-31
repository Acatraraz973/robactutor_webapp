const SUBJECTS = [
  { id: "matematica", label: "Matematică", icon: "Σ" },
  { id: "limba_romana", label: "Limba Română", icon: "Aa" },
  { id: "istorie", label: "Istorie", icon: "⛨" },
  { id: "limba_engleza", label: "Limba Engleză", icon: "GB" },
];

export default function Sidebar({
  t, lang, setLang, activeSubject, setActiveSubject, view, setView, questionsAsked, healthInfo,
}) {
  return (
    <aside className="rail" aria-label="Materii">
      <div className="rail-brand">
        <span className="brand-mark">RB</span>
        <div className="brand-text">
          <span className="brand-name">RoBacTutor</span>
          <span className="brand-sub">Pregătire Bacalaureat</span>
        </div>
      </div>

      <div className="rail-section-label">{t.sectionMode}</div>
      <nav className="subject-tabs">
        <button
          type="button"
          className={"subject-tab" + (view === "practice" ? " is-active" : "")}
          onClick={() => setView("practice")}
        >
          <span className="subject-icon">{"✎"}</span>
          <span>{t.navPractice}</span>
        </button>
        <button
          type="button"
          className={"subject-tab" + (view === "ask" ? " is-active" : "")}
          onClick={() => setView("ask")}
        >
          <span className="subject-icon">{"?"}</span>
          <span>{t.navAsk}</span>
        </button>
      </nav>

      <div className="rail-section-label">{t.sectionSubjects}</div>
      <nav className="subject-tabs">
        {SUBJECTS.map((s) => (
          <button
            key={s.id}
            type="button"
            className={"subject-tab" + (activeSubject === s.id ? " is-active" : "")}
            onClick={() => setActiveSubject(s.id)}
          >
            <span className="subject-icon">{s.icon}</span>
            <span>{s.label}</span>
          </button>
        ))}
      </nav>

      <div className="rail-section-label">{t.sectionSession}</div>
      <div className="rail-meta">
        {healthInfo ? (
          <>
            <span>{healthInfo.question_bank_size} întrebări</span>
            <span className="rail-meta-dot">·</span>
            <span>{healthInfo.chunk_count} fragmente</span>
          </>
        ) : (
          <span>Bacalaureat 2024 – 2025</span>
        )}
      </div>

      <div className="rail-footer">
        {questionsAsked > 0 && (
          <div className="session-counter">
            {t.questionsToday}: {questionsAsked}
          </div>
        )}
        <button
          type="button"
          className={"demo-link" + (view === "demo" ? " is-active" : "")}
          onClick={() => setView("demo")}
        >
          {t.navDemo}
        </button>
        <button className="lang-toggle" type="button" onClick={() => setLang(lang === "ro" ? "en" : "ro")}>
          <span className={"lang-opt" + (lang === "ro" ? " is-active" : "")}>RO</span>
          <span className="lang-divider">/</span>
          <span className={"lang-opt" + (lang === "en" ? " is-active" : "")}>EN</span>
        </button>
      </div>
    </aside>
  );
}
