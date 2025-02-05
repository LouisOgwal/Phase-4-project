import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Home from "./pages/Home";
import Stores from "./pages/Stores";
import Products from "./pages/Products";

function App() {
  return (
    <Router>
      <div className="container">
        <nav>
          <h1>🍏 Apple Store Manager</h1>
          <ul>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/stores">Stores</Link></li>
            <li><Link to="/products">Products</Link></li>
          </ul>
        </nav>

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/stores" element={<Stores />} />
          <Route path="/products" element={<Products />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
