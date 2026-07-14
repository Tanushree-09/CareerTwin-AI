export default function CourseSection({ analysis }) {

  if (!analysis) return null;

  const courses = analysis.courses.recommendations;

  return (

    <section className="bg-[#111827] rounded-2xl shadow-xl border border-slate-700 p-8 transition-all duration-300 hover:border-blue-500">

      <h2 className="text-2xl font-bold text-white mb-6">
        Recommended Courses
      </h2>

      <div className="space-y-5">

        {courses.map((course, index) => (

          <div
            key={index}
            className="bg-[#1E293B] border border-slate-700 rounded-xl p-5 transition-all duration-300 hover:border-blue-500 hover:shadow-lg"
          >

            <div className="flex justify-between items-center">

              <div>

                <h3 className="text-xl font-semibold text-white">
                  {course.title}
                </h3>

                <p className="text-slate-400 mt-1">
                  {course.provider}
                </p>

              </div>

              <span className="bg-blue-900/30 text-blue-300 border border-blue-700 px-3 py-1 rounded-full">
                {course.level}
              </span>

            </div>

            <p className="mt-4 text-slate-300">
              {course.reason}
            </p>

            {course.link && (
              <a
                href={course.link}
                target="_blank"
                rel="noreferrer"
                className="inline-block mt-5 bg-blue-600 hover:bg-blue-500 transition-all duration-300 text-white px-5 py-2 rounded-lg"
              >
                Start Course
              </a>
            )}

          </div>

        ))}

      </div>

    </section>

  );

}