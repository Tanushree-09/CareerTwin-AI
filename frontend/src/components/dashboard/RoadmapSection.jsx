export default function RoadmapSection({ analysis }) {

  if (!analysis) return null;

  const roadmap = analysis.roadmap.roadmap;

  return (

    <section className="bg-[#111827] rounded-2xl shadow-xl border border-slate-700 p-8 transition-all duration-300 hover:border-blue-500">

      <h2 className="text-2xl font-bold text-white mb-6">
        Learning Roadmap
      </h2>

      <div className="space-y-5">

        {roadmap.map((step, index) => (

          <div
            key={index}
            className="bg-[#1E293B] border border-slate-700 border-l-4 border-l-blue-500 rounded-xl pl-5 pr-5 py-4 transition-all duration-300 hover:border-blue-500"
          >

            <h3 className="font-bold text-lg text-white">
              Week {step.week}
            </h3>

            <p className="text-blue-400 font-medium mt-1">
              {step.topic}
            </p>

            <p className="text-slate-300 mt-2 leading-7">
              {step.objective}
            </p>

          </div>

        ))}

      </div>

      <div className="mt-8 bg-blue-900/20 border border-blue-700 rounded-xl p-5">

        <h3 className="font-semibold text-blue-300">
          Final Goal
        </h3>

        <p className="mt-3 text-slate-300 leading-7">
          {analysis.roadmap.final_goal}
        </p>

      </div>

    </section>

  );

}