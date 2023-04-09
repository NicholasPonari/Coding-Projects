import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./Components/App/App";
import reportWebVitals from "./reportWebVitals";

const root = document.getElementById("root");

function randomColor() {
  return "#" + Math.floor(Math.random() * 16777215).toString(16);
}

export default function Root({ loading }) {
  const [color, setColor] = React.useState(randomColor());

  React.useEffect(() => {
    setColor(randomColor());
  }, []);

  React.useEffect(() => {
    if (document.body.style.backgroundColor !== color) {
      document.body.style.backgroundColor = color;
    }
  }, [color, loading]);

  const handleClick = () => {
    setColor(randomColor());
  };

  return <App color={color} loading={loading} handleClick={handleClick} />;
}

ReactDOM.render(
  <React.StrictMode>
    <Root />
  </React.StrictMode>,
  root
);

reportWebVitals();

export { randomColor };
