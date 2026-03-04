import apiClient from './client';

export const getCollections = async () => {
  return await apiClient('collections');
};

export const createCollection = async (data) => {
  return await apiClient('collections', { method: 'POST', body: data });
};

export const deleteCollection = async (id) => {
  return await apiClient(`collections/${id}`, { method: 'DELETE' });
};
