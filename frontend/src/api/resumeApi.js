const BASE_URL = "http://127.0.0.1:8000";

export async function generateResume(data) {
  const res = await fetch(`${BASE_URL}/generate`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });

  return res.json();
}

export async function getATSScore(data) {
  const res = await fetch(`${BASE_URL}/ats-score`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });

  return res.json();
}

export async function getJobMatch(data) {
  const res = await fetch(`${BASE_URL}/job-match`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });

  return res.json();
}