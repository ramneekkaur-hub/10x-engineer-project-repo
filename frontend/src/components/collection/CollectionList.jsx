import React, { useEffect, useState } from 'react';
import { getCollections, deleteCollection } from '../../api/collections';

const CollectionList = ({ onCollectionSelect }) => {
  const [collections, setCollections] = useState([]);

  useEffect(() => {
    const fetchCollections = async () => {
      try {
        const data = await getCollections();
        setCollections(data);
      } catch (error) {
        console.error('Failed to fetch collections:', error);
      }
    };

    fetchCollections();
  }, []);

  const handleDelete = async (id) => {
    if (window.confirm('Are you sure you want to delete this collection?')) {
      try {
        await deleteCollection(id);
        setCollections(collections.filter(collection => collection.id !== id));
      } catch (error) {
        console.error('Failed to delete collection:', error);
      }
    }
  };

  return (
    <div>
      {collections.map(collection => (
        <div key={collection.id}>
          <span onClick={() => onCollectionSelect(collection.id)}>{collection.name}</span>
          <button onClick={() => handleDelete(collection.id)}>Delete</button>
        </div>
      ))}
    </div>
  );
};

export default CollectionList;