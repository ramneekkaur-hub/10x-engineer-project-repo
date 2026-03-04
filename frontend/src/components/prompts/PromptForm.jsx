import React, { useState, useEffect } from 'react';
import { createPrompt, updatePrompt, getPrompt } from '../../api/prompts';
import ErrorMessage from '../shared/ErrorMessage';

const PromptForm = ({ promptId, onSuccess }) => {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const [error, setError] = useState(null);

  useEffect(() => {
    if (promptId) {
      const fetchPrompt = async () => {
        try {
          const prompt = await getPrompt(promptId);
          setTitle(prompt.title);
          setContent(prompt.content);
        } catch (error) {
          setError('Failed to fetch prompt details');
        }
      };

      fetchPrompt();
    }
  }, [promptId]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!title || !content) {
      setError('All fields are required');
      return;
    }

    try {
      if (promptId) {
        await updatePrompt(promptId, { title, content });
      } else {
        await createPrompt({ title, content });
      }
      onSuccess();
    } catch (error) {
      setError('Failed to save the prompt');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      {error && <ErrorMessage message={error} />}
      <input
        type="text"
        value={title}
        onChange={e => setTitle(e.target.value)}
        placeholder="Title"
        required
        aria-label="Prompt Title"
      />
      <textarea
        value={content}
        onChange={e => setContent(e.target.value)}
        placeholder="Content"
        required
        aria-label="Prompt Content"
      />
      <button type="submit" disabled={!title || !content}>
        {promptId ? 'Update' : 'Create'}
      </button>
    </form>
  );
};

export default PromptForm;