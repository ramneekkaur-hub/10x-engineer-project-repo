import React from 'react';

const PromptCard = ({ prompt, onPromptSelect }) => {
  return (
    <div className="prompt-card" onClick={() => onPromptSelect(prompt.id)}>
      <h3>{prompt.title}</h3>
      {/* Additional prompt details */}
    </div>
  );
};

export default PromptCard;