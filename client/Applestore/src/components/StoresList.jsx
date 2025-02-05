import { useEffect, useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

const StoresList = () => {
  const [stores, setStores] = useState([]);


  useEffect(() => {
    fetch("http://localhost:5000/stores")
      .then((res) => res.json())
      .then((data) => setStores(data))
      .catch((error) => console.error("Error fetching stores:", error));
  }, []);

  
  const handleDelete = (id) => {
    fetch(`http://localhost:5000/stores/${id}`, {
      method: "DELETE",
    })
      .then((res) => {
        if (res.ok) {
          setStores((prevStores) => prevStores.filter((store) => store.id !== id));
        }
      })
      .catch((error) => console.error("Error deleting store:", error));
  };

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">Apple Stores</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {stores.map((store) => (
          <Card key={store.id} className="p-4 shadow-lg rounded-lg">
            <CardContent>
              <h3 className="text-lg font-semibold">{store.name}</h3>
              <p className="text-gray-600">{store.address}</p>
              <Button
                className="mt-2 bg-red-500 text-white"
                onClick={() => handleDelete(store.id)}
              >
                Delete Store
              </Button>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
};

export default StoresList;
