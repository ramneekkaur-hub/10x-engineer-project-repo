import React from 'react';
import { deletePrompt } from '../../api/prompts';

const PromptDetail = ({ prompt, onDeleteSuccess }) => {
  const handleDelete = async () => {
    if (window.confirm('Are you sure you want to delete this prompt?')) {
      try {
        await deletePrompt(prompt.id);
        onDeleteSuccess();
      } catch (error) {
        console.error('Failed to delete prompt:', error);
      }
    }
  };

  return (
    <div>
      <h1>{prompt.title}</h1>
      <p>{prompt.content}</p>
      <button onClick={handleDelete}>Delete</button>
    </div>
  );
};

export default PromptDetail;