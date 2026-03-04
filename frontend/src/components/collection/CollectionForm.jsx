import React, { useState } from 'react';
import { createCollection } from '../../api/collections';

const CollectionForm = ({ onCreateSuccess }) => {
  const [name, setName] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await createCollection({ name });
      setName('');
      onCreateSuccess();
    } catch (error) {
      console.error('Failed to create collection:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={name}
        onChange={e => setName(e.target.value)}
        placeholder="Collection Name"
        required
      />
      <button type="submit">Create</button>
    </form>
  );
};

export default CollectionForm;