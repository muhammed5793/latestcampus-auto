import { useEffect, useState } from "react";
import api from "../api/axios";

function StudentDashboard() {
  const [data, setData] = useState(null);

  useEffect(() => {
    api.get("dashboard/student/")
      .then(res => setData(res.data))
      .catch(() => alert("Access denied"));
  }, []);

  if (!data) return <p>Loading...</p>;

  return (
    <div>
      <h2>Student Dashboard</h2>
      <p>Attendance: {data.attendance_percentage}%</p>
      <p>Marks: {data.marks_percentage}%</p>
      <p>Performance: {data.performance_score}</p>
      <p>Status: {data.at_risk ? "⚠ At Risk" : "✅ Safe"}</p>
    </div>
  );
}

export default StudentDashboard;
