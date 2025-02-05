







import { useEffect, useState } from "react";
import axios from "axios";

function Stores() {
  const [stores, setStores] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:5000/stores")
      .then(response => setStores(response.data))
      .catch(error => console.error("Error fetching stores:", error));
  }, []);

  return (
    <div>
      <h2>Stores</h2>
      <ul>
        {stores.map(store => (
          <li key={store.id}>{store.name} - {store.address}</li>
        ))}
      </ul>
    </div>
  );
}

export default Stores;
