function RecognizeFaces() {
  const recognize = () => {
    fetch("http://127.0.0.1:8000/api/ai/recognize/", {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`
      }
    });
  };

  return (
    <div>
      <h3>Recognize Faces</h3>
      <button onClick={recognize}>Start Recognition</button>
    </div>
  );
}

export default RecognizeFaces;
