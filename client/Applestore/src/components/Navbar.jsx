
import React from "react";
import { Link } from "react-router-dom";
import { Button } from "@/components/ui/button";

const Navbar = ({ user, onLogout }) => {
  return (
    <nav className="bg-gray-900 text-white p-4 shadow-md">
      <div className="container mx-auto flex justify-between items-center">

        <Link to="/" className="text-2xl font-bold text-white hover:text-gray-300">
          🍏 Apple Store
        </Link>

    
        <div className="hidden md:flex space-x-6">
          <Link to="/products" className="hover:text-gray-300">Products</Link>
          <Link to="/stores" className="hover:text-gray-300">Stores</Link>
          {user?.isAdmin && <Link to="/admin" className="hover:text-gray-300">Admin</Link>}
        </div>


        <div>
          {user ? (
            <div className="flex items-center space-x-4">
              <span className="text-gray-300">{user.name}</span>
              <Button onClick={onLogout} className="bg-red-600 hover:bg-red-700">Logout</Button>
            </div>
          ) : (
            <Link to="/login">
              <Button className="bg-blue-500 hover:bg-blue-600">Login</Button>
            </Link>
          )}
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
