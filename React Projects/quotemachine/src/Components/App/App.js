import "./App.css";
import Quote from "../Quote/Quote";
import { useState } from "react";

function App({ color, handleClick }) {
  const [loading, setLoading] = useState(false);

  return (
    <div className="wrapper">
      <Quote
        color={color}
        loading={loading}
        setLoading={setLoading}
        handleClick={handleClick}
      />
      <div className="footer">
        <p>by Nicholas Ponari</p>
      </div>
    </div>
  );
}

export default App;
