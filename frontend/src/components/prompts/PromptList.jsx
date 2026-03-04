import React, { useEffect, useState } from 'react';
import PromptCard from './PromptCard';
import { getPrompts } from '../../api/prompts';

const PromptList = ({ onPromptSelect, selectedCollectionId }) => {
  const [prompts, setPrompts] = useState([]);

  useEffect(() => {
    const fetchPrompts = async () => {
      try {
        const data = await getPrompts();
        const filteredPrompts = selectedCollectionId
          ? data.filter(prompt => prompt.collectionId === selectedCollectionId)
          : data;
        setPrompts(filteredPrompts);
      } catch (error) {
        console.error('Failed to fetch prompts:', error);
      }
    };

    fetchPrompts();
  }, [selectedCollectionId]);

  return (
    <div className="prompt-list">
      {prompts.map(prompt => (
        <PromptCard key={prompt.id} prompt={prompt} onPromptSelect={onPromptSelect} />
      ))}
    </div>
  );
};

export default PromptList;