export default function LeetCodeSection({ analysis }) {

  if (!analysis) return null;

    console.log(analysis);
  console.log(analysis.leetcode);

  const problems = analysis.leetcode;

  return (
    <section className="bg-[#111827] border border-slate-700 rounded-2xl shadow-xl p-8">

      <h2 className="text-2xl font-bold text-white mb-2">
        LeetCode Recommendations
      </h2>

      <p className="text-slate-400 mb-8">
        Problems selected specifically for your skill gaps.
      </p>

      <div className="space-y-6">

        {problems.map((problem, index) => (

          <div
            key={index}
            className="bg-slate-800 border border-slate-700 rounded-xl p-6"
          >

            <div className="flex justify-between items-center">

              <div>

                <h3 className="text-xl font-semibold text-white">
                  {problem.title}
                </h3>

                <p className="text-slate-400 mt-2">
                  Difficulty:
                  <span className="ml-2 text-blue-400">
                    {problem.difficulty}
                  </span>
                </p>

                <p className="text-slate-400 mt-1">
                  {problem.topic}
                </p>

              </div>

              <div className="flex gap-3">

                <a
                href={problem.problem_link}
                target="_blank"
                rel="noreferrer"
                className="bg-blue-600 hover:bg-blue-700 px-5 py-2 rounded-lg text-white"
                >
                Solve
                </a>

                {problem.solution_url && (

                  <a
                    href={problem.solution_url}
                    target="_blank"
                    rel="noreferrer"
                    className="bg-green-600 hover:bg-green-700 px-5 py-2 rounded-lg text-white"
                  >
                    Solution
                  </a>

                )}

              </div>

            </div>

          </div>

        ))}

      </div>

    </section>
  );
}