import apiClient from './client';

export const getPrompts = async () => {
  return await apiClient('prompts');
};

export const getPrompt = async (id) => {
  return await apiClient(`prompts/${id}`);
};

export const createPrompt = async (data) => {
  return await apiClient('prompts', { method: 'POST', body: data });
};

export const updatePrompt = async (id, data) => {
  return await apiClient(`prompts/${id}`, { method: 'PUT', body: data });
};

export const deletePrompt = async (id) => {
  return await apiClient(`prompts/${id}`, { method: 'DELETE' });
};
