const BASE_URL = 'https://silver-enigma-g49rg6p9x9vwcq4p-8000.app.github.dev/'; // Updated to the GitHub Codespaces forwarded URL
const apiClient = async (endpoint, { method = 'GET', body, headers } = {}) => {
  const config = {
    method,
    headers: {
      'Content-Type': 'application/json',
      ...headers,
    },
  };

  if (body) {
    config.body = JSON.stringify(body);
  }

  try {
    const response = await fetch(`${BASE_URL}${endpoint}`, config);
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.message || 'Something went wrong');
    }
    return await response.json();
  } catch (error) {
    console.error('API Client Error:', error);
    throw error;
  }
};

export default apiClient;

