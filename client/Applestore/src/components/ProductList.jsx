import axios from "axios";

function ProductList({ products, setProducts }) {
  const handleDelete = (id) => {
    axios.delete(`http://localhost:5000/products/${id}`)
      .then(() => setProducts(prev => prev.filter(product => product.id !== id)))
      .catch(error => console.error("Error deleting product:", error));
  };

  return (
    <ul>
      {products.map(product => (
        <li key={product.id}>
          {product.name} - {product.description}
          <button onClick={() => handleDelete(product.id)}>Delete</button>
        </li>
      ))}
    </ul>
  );
}

export default ProductList;
