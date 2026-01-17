function Alerts() {
  const sendAlerts = () => {
    fetch("http://127.0.0.1:8000/api/performance/send-alerts/", {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`
      }
    });
  };

  return (
    <div>
      <h3>Risk Alerts</h3>
      <button onClick={sendAlerts}>Send Alerts</button>
    </div>
  );
}

export default Alerts;
