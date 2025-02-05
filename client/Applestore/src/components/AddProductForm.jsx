import { useState } from "react";
import axios from "axios";

function AddProductForm() {
  const [price, setPrice] = useState("");
  const [productId, setProductId] = useState("");
  const [storeId, setStoreId] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post("http://localhost:5000/store_products", { price, product_id: productId, store_id: storeId })
      .then(response => console.log("Added:", response.data))
      .catch(error => console.error("Error adding product:", error));
  };

  return (
    <form onSubmit={handleSubmit}>
      <h3>Add Product to Store</h3>
      <input type="number" value={price} onChange={(e) => setPrice(e.target.value)} placeholder="Price" required />
      <input type="number" value={productId} onChange={(e) => setProductId(e.target.value)} placeholder="Product ID" required />
      <input type="number" value={storeId} onChange={(e) => setStoreId(e.target.value)} placeholder="Store ID" required />
      <button type="submit">Add</button>
    </form>
  );
}

export default AddProductForm;
