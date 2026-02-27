import { useState } from "react";

export default function ResumeForm({ onGenerate }) {
  const [form, setForm] = useState({
    name: "",
    education: "",
    skills: "",
    projects: "",
    experience: "",
    achievements: "",
    target_role: "",
    job_description: "",
    });

  function handleChange(e) {
    setForm({ ...form, [e.target.name]: e.target.value });
  }

  function handleSubmit(e) {
    e.preventDefault();
    const formattedData = {
    ...form,
    skills: form.skills.split(",").map(s => s.trim()),
    projects: form.projects.split(",").map(p => p.trim())
    };

    onGenerate(formattedData);
  }

  return (
    <form onSubmit={handleSubmit} className="form">
      <h2>AI Resume Builder</h2>

      {Object.keys(form).map((key) => (
        <textarea
          key={key}
          name={key}
          placeholder={key.replace("_", " ").toUpperCase()}
          value={form[key]}
          onChange={handleChange}
          required
        />
      ))}

      <button type="submit">Generate</button>
    </form>
  );
}