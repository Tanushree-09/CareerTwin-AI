export default function SkillGapSection({ analysis }) {

  if (!analysis) return null;

  const gap = analysis.skill_gap;

  return (
    <section className="bg-[#111827] rounded-2xl shadow-xl border border-slate-700 p-8 transition-all duration-300 hover:border-blue-500">

      <h2 className="text-2xl font-bold text-white mb-6">
        Skill Gap Analysis
      </h2>

      <div className="grid md:grid-cols-2 gap-8">

        <div>

          <h3 className="text-green-300 font-semibold mb-3">
            Existing Skills
          </h3>

          <div className="flex flex-wrap gap-2">

            {gap.existing_skills.map((skill, index) => (
              <span
                key={index}
                className="bg-green-900/20 border border-green-700 text-green-300 px-3 py-1 rounded-full"
              >
                {skill}
              </span>
            ))}

          </div>

        </div>

        <div>

          <h3 className="text-red-300 font-semibold mb-3">
            Missing Skills
          </h3>

          <div className="flex flex-wrap gap-2">

            {gap.missing_skills.map((skill, index) => (
              <span
                key={index}
                className="bg-red-900/20 border border-red-700 text-red-300 px-3 py-1 rounded-full"
              >
                {skill}
              </span>
            ))}

          </div>

        </div>

      </div>

      <div className="mt-8">

        <h3 className="text-blue-300 font-semibold mb-3">
          Priority Skills
        </h3>

        <div className="flex flex-wrap gap-2">

          {gap.priority_skills.map((skill, index) => (
            <span
              key={index}
              className="bg-blue-900/20 border border-blue-700 text-blue-300 px-3 py-1 rounded-full"
            >
              {skill}
            </span>
          ))}

        </div>

      </div>

      <div className="mt-8 bg-[#1E293B] border border-slate-700 rounded-xl p-5">

        <h3 className="font-semibold text-white mb-2">
          AI Explanation
        </h3>

        <p className="text-slate-300 leading-7">
          {gap.explanation}
        </p>

      </div>

    </section>
  );
}