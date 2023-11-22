import React, { useState, useEffect } from 'react';
import { inventorySchema } from '../../sharedDependencies';
import './styles/main.css';

const Inventory = () => {
  const [inventory, setInventory] = useState(inventorySchema);

  useEffect(() => {
    // Fetch inventory data from the backend when the component mounts
    const fetchInventory = async () => {
      try {
        const response = await fetch('/api/inventory');
        const data = await response.json();
        setInventory(data);
      } catch (error) {
        console.error('Failed to fetch inventory:', error);
      }
    };

    fetchInventory();
  }, []);

  const handleItemUse = (itemId) => {
    // Implement item use functionality here
    console.log(`Item with ID ${itemId} used`);
    // Update the inventory state and backend after item use
  };

  const handleItemDiscard = (itemId) => {
    // Implement item discard functionality here
    console.log(`Item with ID ${itemId} discarded`);
    // Update the inventory state and backend after item discard
  };

  return (
    <div className="inventory-grid" id="inventory-grid">
      {inventory.items.map((item) => (
        <div key={item.id} className="inventory-item">
          <img src={item.image} alt={item.name} />
          <div className="item-info">
            <h3>{item.name}</h3>
            <p>{item.description}</p>
            <button onClick={() => handleItemUse(item.id)}>Use</button>
            <button onClick={() => handleItemDiscard(item.id)}>Discard</button>
          </div>
        </div>
      ))}
    </div>
  );
};

export default Inventory;