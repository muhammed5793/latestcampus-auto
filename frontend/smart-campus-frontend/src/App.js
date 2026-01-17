import Login from "./auth/Login";
import StudentDashboard from "./dashboard/StudentDashboard";
import ProfessorDashboard from "./dashboard/ProfessorDashboard";
import AdminDashboard from "./dashboard/AdminDashboard";

function App() {
  const token = localStorage.getItem("token");
  const role = localStorage.getItem("role");

  // 🔐 Not logged in
  if (!token || !role) {
    return <Login />;
  }

  // 🎓 Student
  if (role === "STUDENT") {
    return <StudentDashboard />;
  }

  // 👨‍🏫 Professor
  if (role === "PROFESSOR") {
    return <ProfessorDashboard />;
  }

  // 🧑‍💼 Admin
  if (role === "ADMIN") {
    return <AdminDashboard />;
  }

  // ❌ Invalid role → force logout
  localStorage.clear();
  return <Login />;
}

export default App;
