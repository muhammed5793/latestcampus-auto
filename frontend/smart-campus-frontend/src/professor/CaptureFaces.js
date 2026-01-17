function CaptureFaces() {
  const startCapture = () => {
    fetch("http://127.0.0.1:8000/api/ai/capture/", {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`
      }
    });
  };

  return (
    <div>
      <h3>Capture Faces</h3>
      <button onClick={startCapture}>Start Camera</button>
    </div>
  );
}

export default CaptureFaces;
