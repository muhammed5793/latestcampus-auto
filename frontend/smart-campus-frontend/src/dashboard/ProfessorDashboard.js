import CaptureFaces from "../professor/CaptureFaces";
import TrainModel from "../professor/TrainModel";
import RecognizeFaces from "../professor/RecognizeFaces";
import Alerts from "../professor/Alerts";

function ProfessorDashboard() {
  return (
    <div>
      <h2>Professor Dashboard</h2>
      <CaptureFaces />
      <TrainModel />
      <RecognizeFaces />
      <Alerts />
    </div>
  );
}

export default ProfessorDashboard;
