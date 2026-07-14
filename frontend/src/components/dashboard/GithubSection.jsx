export default function GithubSection({ analysis }) {

  if (!analysis) return null;

  const github = analysis.github;
  const verification = analysis.verification;

  return (
    <section
      id="github"
      className="bg-[#111827] rounded-2xl shadow-xl border border-slate-700 p-8 transition-all duration-300 hover:border-blue-500"
    >

      <div className="flex justify-between items-center mb-8">

        <div>

          <h2 className="text-2xl font-bold text-white">
            GitHub Analysis
          </h2>

          <p className="text-slate-400 mt-2">
            Skills verified using your repositories
          </p>

        </div>

        <a
          href={github.profile_url}
          target="_blank"
          rel="noreferrer"
          className="bg-blue-600 hover:bg-blue-700 transition px-5 py-2 rounded-xl text-white font-medium"
        >
          View GitHub
        </a>

      </div>

      {/* Statistics */}

      <div className="grid md:grid-cols-4 gap-5 mb-8">

        <div className="bg-[#1E293B] border border-slate-700 rounded-xl p-5">

          <h3 className="text-slate-400">
            Repositories
          </h3>

          <p className="text-4xl font-bold text-cyan-400 mt-3">
            {github.total_repositories}
          </p>

        </div>

        <div className="bg-[#1E293B] border border-slate-700 rounded-xl p-5">

          <h3 className="text-slate-400">
            Languages
          </h3>

          <p className="text-4xl font-bold text-green-400 mt-3">
            {Object.keys(github.languages).length}
          </p>

        </div>

        <div className="bg-[#1E293B] border border-slate-700 rounded-xl p-5">

          <h3 className="text-slate-400">
            Stars
          </h3>

          <p className="text-4xl font-bold text-yellow-400 mt-3">
            {github.total_stars}
          </p>

        </div>

        <div className="bg-[#1E293B] border border-slate-700 rounded-xl p-5">

          <h3 className="text-slate-400">
            Verified Skills
          </h3>

          <p className="text-4xl font-bold text-purple-400 mt-3">
            {verification.verified_skills.length}
          </p>

        </div>

      </div>

      {/* Skills */}

      <div className="grid lg:grid-cols-2 gap-6">

        <div className="bg-green-900/20 border border-green-700 rounded-xl p-6">

          <h3 className="text-xl font-semibold text-green-300 mb-5">
            Verified Skills
          </h3>

          <div className="flex flex-wrap gap-3">

            {verification.verified_skills.map(skill => (

              <span
                key={skill}
                className="bg-green-500/20 border border-green-500 text-green-300 px-4 py-2 rounded-full"
              >
                {skill}
              </span>

            ))}

          </div>

        </div>

        <div className="bg-blue-900/20 border border-blue-700 rounded-xl p-6">

          <h3 className="text-xl font-semibold text-blue-300 mb-5">
            Additional Skills Detected
          </h3>

          <div className="flex flex-wrap gap-3">

            {verification.additional_detected_skills.map(skill => (

              <span
                key={skill}
                className="bg-blue-500/20 border border-blue-500 text-blue-300 px-4 py-2 rounded-full"
              >
                {skill}
              </span>

            ))}

          </div>

        </div>

      </div>

    </section>
  );
}