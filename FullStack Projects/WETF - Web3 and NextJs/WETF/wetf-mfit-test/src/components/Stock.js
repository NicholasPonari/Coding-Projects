const Stock = ({ stock, price }) => {
  return (
    <div class="stock">
      <h2>{stock}</h2>
      <p>${price}</p>
    </div>
  );
};
export default Stock;
