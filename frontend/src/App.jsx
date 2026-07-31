import { useEffect, useState } from "react";
import Sidebar from "./components/Sidebar";
import PracticeScreen from "./components/PracticeScreen";
import AskScreen from "./components/AskScreen";
import DemoScreen from "./components/DemoScreen";
import { STRINGS } from "./i18n";
import { fetchHealth } from "./api";

function makeSessionId() {
  return typeof crypto !== "undefined" && crypto.randomUUID
    ? crypto.randomUUID()
    : `session-${Date.now()}-${Math.random().toString(16).slice(2)}`;
}

export default function App() {
  const [lang, setLang] = useState("ro");
  const [activeSubject, setActiveSubject] = useState("matematica");
  const [view, setView] = useState("practice"); // 'practice' | 'ask' | 'demo'
  const [healthInfo, setHealthInfo] = useState(null);
  const [questionsAsked, setQuestionsAsked] = useState(0);
  const [sessionId] = useState(makeSessionId);

  const t = STRINGS[lang];
  const bumpQuestionsAsked = () => setQuestionsAsked((n) => n + 1);

  useEffect(() => {
    fetchHealth()
      .then(setHealthInfo)
      .catch((err) => console.error("Could not reach backend /api/health:", err));
  }, []);

  return (
    <div className="app-shell">
      <Sidebar
        t={t}
        lang={lang}
        setLang={setLang}
        activeSubject={activeSubject}
        setActiveSubject={setActiveSubject}
        view={view}
        setView={setView}
        questionsAsked={questionsAsked}
        healthInfo={healthInfo}
      />
      {view === "practice" && (
        <PracticeScreen t={t} subject={activeSubject} sessionId={sessionId} onAnswered={bumpQuestionsAsked} />
      )}
      {view === "ask" && (
        <AskScreen t={t} subject={activeSubject} onAsked={bumpQuestionsAsked} />
      )}
      {view === "demo" && (
        <DemoScreen t={t} subject={activeSubject} sessionId={sessionId} />
      )}
    </div>
  );
}
