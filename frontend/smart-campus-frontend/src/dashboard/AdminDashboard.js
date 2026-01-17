import { useEffect, useState } from "react";
import api from "../api/axios";
import LogoutButton from "../components/LogoutButton";

function AdminDashboard() {
  const [stats, setStats] = useState(null);

  useEffect(() => {
    api.get("dashboard/admin/")
      .then(res => setStats(res.data))
      .catch(() => alert("Access denied"));
  }, []);

  if (!stats) return <p>Loading...</p>;

  return (
    <div>
      {/* Logout button placed at the top */}
      <LogoutButton />

      <h2>Admin Dashboard</h2>
      <p>Total Students: {stats.total_students}</p>
      <p>Average Performance: {stats.average_performance}</p>
      <p>At-Risk Count: {stats.at_risk_count}</p>
    </div>
  );
}

export default AdminDashboard;