export default function OverviewCards({ analysis }) {

  if (!analysis) {
    return (
      <div className="bg-yellow-900/20 border border-yellow-700 text-yellow-300 p-4 rounded-xl">
        Waiting for analysis...
      </div>
    );
  }

  return (
    <div className="grid grid-cols-4 gap-6">

      <div className="bg-[#111827] border border-slate-700 rounded-2xl shadow-xl p-6 transition-all duration-300 hover:border-blue-500">

        <h3 className="text-slate-400">
          Career Readiness
        </h3>

        <p className="text-4xl font-bold text-blue-400 mt-3">
          {analysis.career.overall_score}%
        </p>

      </div>

      <div className="bg-[#111827] border border-slate-700 rounded-2xl shadow-xl p-6 transition-all duration-300 hover:border-cyan-500">

        <h3 className="text-slate-400">
          Skills
        </h3>

        <p className="text-4xl font-bold text-cyan-400 mt-3">
          {analysis.profile.skills.length}
        </p>

      </div>

      <div className="bg-[#111827] border border-slate-700 rounded-2xl shadow-xl p-6 transition-all duration-300 hover:border-red-500">

        <h3 className="text-slate-400">
          Missing Skills
        </h3>

        <p className="text-4xl font-bold text-red-400 mt-3">
          {analysis.skill_gap.missing_skills.length}
        </p>

      </div>

      <div className="bg-[#111827] border border-slate-700 rounded-2xl shadow-xl p-6 transition-all duration-300 hover:border-green-500">

        <h3 className="text-slate-400">
          Projects
        </h3>

        <p className="text-4xl font-bold text-green-400 mt-3">
          {analysis.projects.projects.length}
        </p>

      </div>

    </div>
  );

}