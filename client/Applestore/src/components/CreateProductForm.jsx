import { useState } from "react";
import axios from "axios";

function CreateProductForm({ setProducts }) {
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post("http://localhost:5000/products", { name, description })
      .then(response => {
        setProducts(prevProducts => [...prevProducts, response.data]);
        setName("");
        setDescription("");
      })
      .catch(error => console.error("Error creating product:", error));
  };

  return (
    <form onSubmit={handleSubmit} className="p-4 border rounded shadow-md">
      <h3 className="text-lg font-bold mb-2">Create New Product</h3>
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Product Name"
        required
        className="w-full p-2 border rounded mb-2"
      />
      <textarea
        value={description}
        onChange={(e) => setDescription(e.target.value)}
        placeholder="Product Description"
        required
        className="w-full p-2 border rounded mb-2"
      />
      <button type="submit" className="bg-blue-500 text-white p-2 rounded">
        Create Product
      </button>
    </form>
  );
}

export default CreateProductForm;
