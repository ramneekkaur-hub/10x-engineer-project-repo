import React from 'react';

const PromptCard = ({ prompt, onEdit, onDelete, onSelect }) => {
  return (
    <div className="prompt-card">
      <h3>{prompt.title}</h3>
      <p>{prompt.content}</p>
      <button onClick={(e) => { e.stopPropagation(); onEdit(prompt.id); }}>Edit</button>
      <button onClick={(e) => { e.stopPropagation(); onDelete(prompt.id); }}>Delete</button>
      <button onClick={(e) => { e.stopPropagation(); onSelect(prompt.id); }}>View</button>
    </div>
  );
};

export default PromptCard;