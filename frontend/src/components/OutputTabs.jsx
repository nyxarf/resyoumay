import { useState } from "react";

export default function OutputTabs({ result }) {
  const [tab, setTab] = useState("resume");

  if (!result) return null;

  return (
    <div className="output">
      <div className="tabs">
        {["resume", "cover_letter", "portfolio_summary", "ats_keywords"].map(
          (t) => (
            <button key={t} onClick={() => setTab(t)}>
              {t.replace("_", " ").toUpperCase()}
            </button>
          )
        )}
      </div>

      <div className="content">
        {Array.isArray(result[tab])
          ? result[tab].join(", ")
          : result[tab]}
      </div>
    </div>
  );
}