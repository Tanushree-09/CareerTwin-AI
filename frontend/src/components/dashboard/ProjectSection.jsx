export default function ProjectSection({ analysis }) {

  if (!analysis) return null;

  const projects = analysis.projects.projects;

  return (
    <section
      id="projects"
      className="bg-[#111827] rounded-2xl shadow-xl border border-slate-700 p-8 transition-all duration-300 hover:border-blue-500"
    >

      <div className="flex justify-between items-center mb-8">

        <div>

          <h2 className="text-2xl font-bold text-white">
            Project Analysis
          </h2>

          <p className="text-slate-400 mt-2">
            AI evaluation of your portfolio projects
          </p>

        </div>

      </div>

      <div className="space-y-8">

        {projects.map((project) => (

          <div
            key={project.project_name}
            className="bg-[#1E293B] border border-slate-700 rounded-2xl p-6 transition-all duration-300 hover:border-cyan-500 hover:shadow-xl"
          >

            <div className="flex justify-between items-center mb-6">

              <div>

                <h3 className="text-2xl font-bold text-white">
                  {project.project_name}
                </h3>

                <p className="text-slate-400 mt-2">

                  Resume Ready{" "}
                  <span
                    className={
                      project.resume_ready
                        ? "text-green-400 font-semibold"
                        : "text-red-400 font-semibold"
                    }
                  >
                    {project.resume_ready ? "✅ Yes" : "❌ No"}
                  </span>

                </p>

              </div>

              <div className="text-center">

                <p className="text-slate-400">
                  Project Score
                </p>

                <p className="text-5xl font-bold text-blue-400 mt-2">
                  {project.score}/10
                </p>

              </div>

            </div>

            <div className="grid lg:grid-cols-2 gap-6">

              <div className="bg-green-900/20 border border-green-700 rounded-xl p-5">

                <h4 className="font-semibold text-green-300 mb-4">
                  Strengths
                </h4>

                <ul className="list-disc ml-5 space-y-2 text-slate-300">

                  {project.strengths.map(item => (
                    <li key={item}>{item}</li>
                  ))}

                </ul>

              </div>

              <div className="bg-red-900/20 border border-red-700 rounded-xl p-5">

                <h4 className="font-semibold text-red-300 mb-4">
                  Weaknesses
                </h4>

                <ul className="list-disc ml-5 space-y-2 text-slate-300">

                  {project.weaknesses.map(item => (
                    <li key={item}>{item}</li>
                  ))}

                </ul>

              </div>

              <div className="bg-yellow-900/20 border border-yellow-700 rounded-xl p-5">

                <h4 className="font-semibold text-yellow-300 mb-4">
                  Missing Features
                </h4>

                <ul className="list-disc ml-5 space-y-2 text-slate-300">

                  {project.missing_features.map(item => (
                    <li key={item}>{item}</li>
                  ))}

                </ul>

              </div>

              <div className="bg-blue-900/20 border border-blue-700 rounded-xl p-5">

                <h4 className="font-semibold text-blue-300 mb-4">
                  AI Recommendations
                </h4>

                <ul className="list-disc ml-5 space-y-2 text-slate-300">

                  {project.recommendations.map(item => (
                    <li key={item}>{item}</li>
                  ))}

                </ul>

              </div>

            </div>

          </div>

        ))}

      </div>

    </section>

  );

}