import React, { useState, useEffect } from 'react';
import { createPrompt, updatePrompt, getPrompt } from '../../api/prompts';

const PromptForm = ({ promptId, onSuccess }) => {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');

  useEffect(() => {
    if (promptId) {
      const fetchPrompt = async () => {
        try {
          const prompt = await getPrompt(promptId);
          setTitle(prompt.title);
          setContent(prompt.content);
        } catch (error) {
          console.error('Failed to fetch prompt:', error);
        }
      };

      fetchPrompt();
    }
  }, [promptId]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (promptId) {
        await updatePrompt(promptId, { title, content });
      } else {
        await createPrompt({ title, content });
      }
      onSuccess();
    } catch (error) {
      console.error('Failed to save prompt:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={title}
        onChange={e => setTitle(e.target.value)}
        placeholder="Title"
        required
      />
      <textarea
        value={content}
        onChange={e => setContent(e.target.value)}
        placeholder="Content"
        required
      />
      <button type="submit">{promptId ? 'Update' : 'Create'}</button>
    </form>
  );
};

export default PromptForm;