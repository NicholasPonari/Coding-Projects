import { LeafPoll, Result } from "react-leaf-polls";
import "react-leaf-polls/dist/index.css";
import getPrice from "../services/Price";
// Persistent data array (typically fetched from the server)

// Object keys may vary on the poll type (see the 'Theme options' table below)
const customTheme = {
  textColor: "black",
  mainColor: "#00B87B",
  backgroundColor: "rgb(255,255,255)",
  alignment: "center",
};

function vote(item, results) {
  // Here you probably want to manage
  // and return the modified data to the server.
}

const Poll = () => {
  let stocks = [
    {
      id: 0,
      ticker: "GOOG",
      name: "Google",
      voteCount: 5,
      price: 0,
    },
    {
      id: 1,
      ticker: "TSLA",
      name: "Tesla",
      voteCount: 15,
      price: 0,
    },
    {
      id: 2,
      ticker: "NFLX",
      name: "Netflix",
      voteCount: 3,
      price: 0,
    },
    {
      id: 3,
      ticker: "AAPL",
      name: "Apple",
      voteCount: 1,
      price: 0,
    },
  ];

  stocks.forEach((stock) => {
    getPrice(stock.ticker).then((val) => {
      stock.price = val;
    });
  });

  let resData = [];
  stocks.forEach((stock) => {
    resData.push({
      id: stock.id,
      text: `${stock.name} USD $${stock.price}/share`,
      votes: stock.voteCount,
    });
  });

  return (
    <LeafPoll
      type="multiple"
      question="Choose the security that you believe will perform the best for the
      week of December 5th, 2022"
      results={resData}
      theme={customTheme}
      onVote={vote}
      isVoted={false}
    />
  );
};

export default Poll;
