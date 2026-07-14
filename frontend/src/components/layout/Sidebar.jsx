import {
  LayoutDashboard,
  FileText,
  Brain,
  GraduationCap,
  BookOpen,
  FolderGit2,
  FolderKanban,
  Trophy,
} from "lucide-react";

const menu = [
  { title: "Overview", icon: LayoutDashboard, id: "overview" },
  { title: "Resume Analysis", icon: FileText, id: "resume" },
  { title: "Skill Gap", icon: Brain, id: "skillgap" },
  { title: "Courses", icon: BookOpen, id: "courses" },
  { title: "Learning Roadmap", icon: GraduationCap, id: "roadmap" },
  { title: "GitHub Analysis", icon: FolderGit2, id: "github" },
  { title: "Projects", icon: FolderKanban, id: "projects" },
  { title: "Career Readiness", icon: Trophy, id: "career" },
];

export default function Sidebar() {
  const scrollToSection = (id) => {
    const section = document.getElementById(id);

    if (section) {
      section.scrollIntoView({
        behavior: "smooth",
      });
    }
  };

  return (
    <aside className="sticky top-0 h-screen w-72 bg-slate-900 text-white shadow-xl">

      <div className="p-8 border-b border-slate-700">

        <h1 className="text-3xl font-bold">
          CareerTwin AI
        </h1>

        <p className="text-slate-400 mt-2 text-sm">
          Your Personal AI Career Mentor
        </p>

      </div>

      <nav className="mt-6 px-4">

        {menu.map((item) => (

          <button
            key={item.title}
            onClick={() => scrollToSection(item.id)}
            className="flex items-center gap-4 w-full rounded-xl px-4 py-3 text-left hover:bg-slate-800 transition mb-2"
          >

            <item.icon size={20} />

            <span>{item.title}</span>

          </button>

        ))}

      </nav>

    </aside>
  );
}