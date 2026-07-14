import Sidebar from "../components/layout/Sidebar";
import { useState } from "react";
import TopPanel from "../components/dashboard/TopPanel";
import OverviewCards from "../components/dashboard/OverviewCards";
import ResumeSection from "../components/dashboard/ResumeSection";
import SkillGapSection from "../components/dashboard/SkillGapSection";
import CourseSection from "../components/dashboard/CourseSection";
import RoadmapSection from "../components/dashboard/RoadmapSection";
import GithubSection from "../components/dashboard/GithubSection";
import ProjectSection from "../components/dashboard/ProjectSection";
import CareerSection from "../components/dashboard/CareerSection";
import LeetCodeSection from "../components/dashboard/LeetCodeSection";

export default function Dashboard() {
  const [analysis, setAnalysis] = useState(null);
  return (
    <div className="flex bg-[#0B1120] min-h-screen text-white">

      <Sidebar />

      <main className="flex-1 overflow-y-auto bg-[#0B1120]">

        <div className="max-w-7xl mx-auto p-8 space-y-8">

          <TopPanel setAnalysis={setAnalysis} />
          

          <OverviewCards analysis={analysis} />

          <ResumeSection analysis={analysis} />

          <SkillGapSection analysis={analysis} />

          <CourseSection analysis={analysis} />

          <RoadmapSection analysis={analysis} />

          <LeetCodeSection analysis={analysis} />

          <GithubSection analysis={analysis} />

          <ProjectSection analysis={analysis} />

          <CareerSection analysis={analysis} />

        </div>

      </main>

    </div>
  );
}