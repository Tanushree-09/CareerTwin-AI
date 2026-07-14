import api from "../../api/api";
import { useState } from "react";

export default function TopPanel({ setAnalysis }) {

  const [careerGoal, setCareerGoal] = useState("AI Engineer");
  const [timeline, setTimeline] = useState("6 Months");
  const [github, setGithub] = useState("");
  const [resume, setResume] = useState(null);

  const handleAnalyze = async () => {

    console.log("1. Function started");

    if (!resume) {
      alert("Please upload a resume.");
      return;
    }

    const formData = new FormData();

    formData.append("resume", resume);
    formData.append("github", github);
    formData.append("career_goal", careerGoal);
    formData.append("timeline", timeline);

    try {

      const response = await api.post("/analyze", formData);

      setAnalysis(response.data);

      alert("Analysis Complete!");

    } catch (error) {

      console.error(error);

      alert("Something went wrong.");

    }

  };

  return (

    <section className="bg-[#111827] border border-slate-700 rounded-2xl shadow-xl p-8 transition-all duration-300 hover:border-blue-500">

      <h1 className="text-4xl font-bold text-white">
        Career Analysis
      </h1>

      <p className="text-slate-400 mt-2 mb-8">
        Upload your resume and GitHub profile to receive a personalized AI-powered career roadmap.
      </p>

      <div className="grid grid-cols-2 gap-6">

        {/* Career Goal */}

        <div>

          <label className="font-semibold text-slate-200">
            Target Career
          </label>

          <select
            value={careerGoal}
            onChange={(e) => setCareerGoal(e.target.value)}
            className="mt-2 w-full rounded-xl bg-[#1E293B] border border-slate-700 text-white p-3 focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            <option>AI Engineer</option>
            <option>Machine Learning Engineer</option>
            <option>Data Scientist</option>
            <option>Software Engineer</option>
            <option>Backend Developer</option>
            <option>Frontend Developer</option>
            <option>Full Stack Developer</option>
          </select>

        </div>

        {/* Timeline */}

        <div>

          <label className="font-semibold text-slate-200">
            Target Timeline
          </label>

          <select
            value={timeline}
            onChange={(e) => setTimeline(e.target.value)}
            className="mt-2 w-full rounded-xl bg-[#1E293B] border border-slate-700 text-white p-3 focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            <option>3 Months</option>
            <option>6 Months</option>
            <option>12 Months</option>
          </select>

        </div>

        {/* GitHub */}

        <div className="col-span-2">

          <label className="font-semibold text-slate-200">
            GitHub Username
          </label>

          <input
            type="text"
            value={github}
            onChange={(e) => setGithub(e.target.value)}
            placeholder="Your Username Here"
            className="mt-2 w-full rounded-xl bg-[#1E293B] border border-slate-700 text-white placeholder-slate-500 p-3 focus:outline-none focus:ring-2 focus:ring-blue-500"
          />

        </div>

        {/* Resume */}

        <div className="col-span-2">

          <label className="font-semibold text-slate-200">
            Upload Resume (PDF)
          </label>

          <input
            type="file"
            accept=".pdf"
            onChange={(e) => setResume(e.target.files[0])}
            className="mt-2 w-full rounded-xl bg-[#1E293B] border border-slate-700 text-slate-300 file:bg-blue-600 file:text-white file:border-0 file:px-4 file:py-2 file:rounded-lg file:mr-4"
          />

          {resume && (

            <p className="mt-3 text-green-400 text-sm">
              ✓ Selected: {resume.name}
            </p>

          )}

        </div>

      </div>

      <button
        onClick={handleAnalyze}
        className="mt-8 bg-blue-600 hover:bg-blue-500 transition-all duration-300 text-white px-8 py-4 rounded-xl font-semibold shadow-lg hover:scale-105"
      >
        Analyze Career
      </button>

    </section>

  );

}