const BASE_URL = 'https://your-api-base-url.com/'; // Replace with your actual API base URL

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
