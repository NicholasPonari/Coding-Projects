const getPrice = async (stock) => {
  const response = await fetch(
    `https://cloud.iexapis.com/v1/data/CORE/QUOTE/${stock}?token=sk_b31469b47dc247f7adc3347f9f2c89b2`
  );
  const stockInfo = await response.text();
  const stockPrice = JSON.parse(stockInfo);

  return stockPrice[0]["previousClose"];
};

export default getPrice;
