import React, { useEffect, useState } from 'react';
import PromptCard from './PromptCard';
import PromptForm from './PromptForm';
import { getPrompts, deletePrompt } from '../../api/prompts';

const PromptList = ({ searchQuery, onPromptUpdate }) => {
  const [prompts, setPrompts] = useState([]);
  const [editingPromptId, setEditingPromptId] = useState(null);

  const fetchPrompts = async () => {
    try {
      const data = await getPrompts();
      setPrompts(Array.isArray(data) ? data : []);
    } catch (error) {
      console.error('Failed to load prompts:', error);
      setPrompts([]);
    }
  };

  useEffect(() => {
    fetchPrompts();
  }, []);

  const handleEdit = (id) => {
    setEditingPromptId(id);
  };
  
  const handleDelete = async (id) => {
    try {
      await deletePrompt(id);
      onPromptUpdate('Prompt deleted successfully!');
      fetchPrompts(); // Refresh prompts after deletion
    } catch (error) {
      console.error('Failed to delete prompt:', error);
    }
  };

  const handleFormSuccess = () => {
    setEditingPromptId(null);
    fetchPrompts();
    onPromptUpdate('Prompt updated successfully!');
  };

  const filteredPrompts = prompts.filter(prompt =>
    prompt.title && prompt.title.toLowerCase().includes(searchQuery.toLowerCase())
  );

  return (
    <div>
      {editingPromptId && (
        <PromptForm promptId={editingPromptId} onSuccess={handleFormSuccess} />
      )}
      <div className="prompt-list">
        {filteredPrompts.map(prompt => (
          <PromptCard
            key={prompt.id}
            prompt={prompt}
            onEdit={handleEdit}
            onDelete={handleDelete}
            onSelect={() => console.log('Prompt selected:', prompt.id)}
          />
        ))}
      </div>
    </div>
  );
};

export default PromptList;
