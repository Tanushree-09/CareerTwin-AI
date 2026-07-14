export default function ResumeSection({ analysis }) {

  if (!analysis) return null;

  const feedback = analysis.resume_feedback;

  return (
    <div className="bg-[#111827] rounded-2xl shadow-xl border border-slate-700 p-6 transition-all duration-300 hover:border-blue-500">

      <h2 className="text-2xl font-bold text-white mb-4">
        Resume Analysis
      </h2>

      <p className="mb-6 text-slate-300">

        Overall Resume Score:

        <span className="font-bold text-blue-400 text-xl ml-2">
          {feedback.overall_score}/100
        </span>

      </p>

      <div className="grid grid-cols-2 gap-8">

        <div className="bg-green-900/20 border border-green-700 rounded-xl p-5">

          <h3 className="font-semibold text-green-300 mb-3">
            Strengths
          </h3>

          <ul className="list-disc ml-6 space-y-2 text-slate-300">

            {feedback.strengths.map((item, index) => (
              <li key={index}>{item}</li>
            ))}

          </ul>

        </div>

        <div className="bg-red-900/20 border border-red-700 rounded-xl p-5">

          <h3 className="font-semibold text-red-300 mb-3">
            Weaknesses
          </h3>

          <ul className="list-disc ml-6 space-y-2 text-slate-300">

            {feedback.weaknesses.map((item, index) => (
              <li key={index}>{item}</li>
            ))}

          </ul>

        </div>

      </div>

    </div>
  );

}