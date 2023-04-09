const http = require("http");

http
  .createServer(function (req, res) {
    res.setHeader("Access-Control-Allow-Origin", "*");
    res.setHeader("Content-Type", "application/json");

    fetch(
      "https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en"
    )
      .then((response) => response.json())
      .then((data) => res.end(JSON.stringify(data)))
      .catch((err) => console.error(err));
  })
  .listen(3001);
