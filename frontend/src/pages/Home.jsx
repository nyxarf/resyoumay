import { useState } from "react";
import ResumeForm from "../components/ResumeForm";
import OutputTabs from "../components/OutputTabs";
import DownloadButtons from "../components/DownloadButtons";
import {
  generateResume,
  getATSScore,
  getJobMatch
} from "../api/resumeApi";

export default function Home() {
  const [result, setResult] = useState(null);
  const [ats, setAts] = useState(null);
  const [match, setMatch] = useState(null);

  async function handleGenerate(data) {
    const res = await generateResume(data);

    setResult(res);

    // ✅ ATS Score
    const atsResult = await getATSScore({
      resume_text: res.resume,
      skills: data.skills,
      target_role: data.job_role
    });

    setAts(atsResult);

    // ✅ Job Match Score
    const matchResult = await getJobMatch({
      resume_text: res.resume,
      job_description: data.job_description
    });

    setMatch(matchResult);
  }

  return (
    <div className="container">
      <ResumeForm onGenerate={handleGenerate} />

      {/* Generated Outputs */}
      <OutputTabs result={result} />
      <DownloadButtons result={result} />

      {/* ⭐ ADD YOUR CODE HERE ⭐ */}

      {ats && (
        <div className="score-box">
          <h3>ATS Score: {ats.ats_score}%</h3>
          <p>{ats.verdict}</p>
        </div>
      )}

      {match && (
        <div className="score-box">
          <h3>Job Match Score: {match.job_match_score}%</h3>
          <p>{match.recommendation}</p>
        </div>
      )}
    </div>
  );
}