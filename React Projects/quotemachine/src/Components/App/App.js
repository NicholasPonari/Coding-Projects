import "./App.css";
import Quote from "../Quote/Quote";

function App({ color }) {
  return (
    <div className="wrapper">
      <Quote color={color} />
      <div className="footer">
        <p>by Nicholas Ponari</p>
      </div>
    </div>
  );
}

export default App;
