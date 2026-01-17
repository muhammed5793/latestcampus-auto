function TrainModel() {
  const train = () => {
    fetch("http://127.0.0.1:8000/api/ai/train/", {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`
      }
    });
  };

  return (
    <div>
      <h3>Train Model</h3>
      <button onClick={train}>Start Training</button>
    </div>
  );
}

export default TrainModel;
