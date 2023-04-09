import "./Quote.css";
import { FaQuoteLeft } from "react-icons/fa";
import { FaTwitter } from "react-icons/fa";
import { useState, useEffect } from "react";

function Quote({ color, loading, setLoading, handleClick }) {
  const [quote, setQuote] = useState("");
  const [author, setAuthor] = useState("");

  useEffect(() => {
    fetch("http://localhost:3001/quote")
      .then((response) => response.json())
      .then((data) => {
        setQuote(data.quoteText);
        setAuthor(data.quoteAuthor);
      })
      .catch((error) => console.log(error));
  }, []);

  const handleNewQuote = () => {
    setLoading(true);
    handleClick();
    setQuote("");
    setAuthor("");
    fetch("http://localhost:3001/quote")
      .then((response) => response.json())
      .then((data) => {
        setQuote(data.quoteText);
        setAuthor(data.quoteAuthor);
        setLoading(false);
      })
      .catch((error) => console.log(error));
  };

  return (
    <div id="quote-box">
      <div id="text" style={{ color: color }}>
        <p>
          <FaQuoteLeft />
          {quote}
        </p>
      </div>
      <div id="author" style={{ color: color }}>
        <p>{author}</p>
      </div>
      <div id="buttons">
        <button id="tweet-quote" style={{ backgroundColor: color }}>
          <FaTwitter />
        </button>
        <button
          id="new-quote"
          style={{ backgroundColor: color }}
          onClick={handleNewQuote}
        >
          New Quote
        </button>
      </div>
    </div>
  );
}

export default Quote;
