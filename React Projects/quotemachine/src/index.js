import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./Components/App/App";
import reportWebVitals from "./reportWebVitals";

const root = ReactDOM.createRoot(document.getElementById("root"));

function randomColor() {
  return "#" + Math.floor(Math.random() * 16777215).toString(16);
}

function Root() {
  const [color, setColor] = React.useState(randomColor());

  React.useEffect(() => {
    setColor(randomColor());
  }, []);

  document.body.style.backgroundColor = color;

  return <App color={color} />;
}

root.render(
  <React.StrictMode>
    <Root />
  </React.StrictMode>
);

reportWebVitals();
