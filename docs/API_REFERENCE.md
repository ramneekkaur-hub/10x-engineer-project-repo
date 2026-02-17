# API Reference

## Health Check

### `GET /health`

- **Description:** Check the health status of the API.
- **Parameters:** None
- **Request Body:** None
- **Response:**

  ```json
  {
    "status": "healthy",
    "version": "1.0.0"
  }
  ```

- **Error Responses:** None
- **Authentication:** None

## Prompt Endpoints

### `GET /prompts`

- **Description:** Retrieve a list of all prompts with optional filtering and search.
- **Parameters:**
  - `collection_id` (optional, query): Filter prompts by collection ID.
  - `search` (optional, query): Search query to filter prompts by title or content.
- **Request Body:** None
- **Response:**

  ```json
  {
    "prompts": [
      {
        "id": "string",
        "title": "string",
        "content": "string",
        "description": "string",
        "collection_id": "string",
        "created_at": "2023-01-01T00:00:00Z",
        "updated_at": "2023-01-01T00:00:00Z"
      }
    ],
    "total": 1
  }
  ```

- **Error Responses:** None
- **Authentication:** None

### `GET /prompts/{prompt_id}`

- **Description:** Retrieve a prompt by its unique identifier.
- **Parameters:**
  - `prompt_id` (path): The unique identifier of the prompt.
- **Request Body:** None
- **Response:**

  ```json
  {
    "id": "string",
    "title": "string",
    "content": "string",
    "description": "string",
    "collection_id": "string",
    "created_at": "2023-01-01T00:00:00Z",
    "updated_at": "2023-01-01T00:00:00Z"
  }
  ```

- **Error Responses:**

  ```json
  {
    "detail": "Prompt not found"
  }
  ```

- **Authentication:** None

### `POST /prompts`

- **Description:** Create a new prompt.
- **Parameters:** None
- **Request Body:**

  ```json
  {
    "title": "string",
    "content": "string",
    "description": "string",
    "collection_id": "string"
  }
  ```

- **Response:**

  ```json
  {
    "id": "string",
    "title": "string",
    "content": "string",
    "description": "string",
    "collection_id": "string",
    "created_at": "2023-01-01T00:00:00Z",
    "updated_at": "2023-01-01T00:00:00Z"
  }
  ```

- **Error Responses:**

  ```json
  {
    "detail": "Collection not found"
  }
  ```

- **Authentication:** None

### `PUT /prompts/{prompt_id}`

- **Description:** Update an entire prompt with new data.
- **Parameters:**
  - `prompt_id` (path): The unique identifier of the prompt.
- **Request Body:**

  ```json
  {
    "title": "string",
    "content": "string",
    "description": "string",
    "collection_id": "string"
  }
  ```

- **Response:**

  ```json
  {
    "id": "string",
    "title": "string",
    "content": "string",
    "description": "string",
    "collection_id": "string",
    "created_at": "2023-01-01T00:00:00Z",
    "updated_at": "2023-01-01T00:00:00Z"
  }
  ```

- **Error Responses:**

  ```json
  {
    "detail": "Prompt not found"
  }
  ```

  or

  ```json
  {
    "detail": "Collection not found"
  }
  ```

- **Authentication:** None

### `PATCH /prompts/{prompt_id}`

- **Description:** Partially update a prompt with only provided fields.
- **Parameters:**
  - `prompt_id` (path): The unique identifier of the prompt.
- **Request Body:** (Partial fields from PromptUpdate)

  ```json
  {
    "title": "string"
  }
  ```

- **Response:**

  ```json
  {
    "id": "string",
    "title": "string",
    "content": "string",
    "description": "string",
    "collection_id": "string",
    "created_at": "2023-01-01T00:00:00Z",
    "updated_at": "2023-01-01T00:00:00Z"
  }
  ```

- **Error Responses:**

  ```json
  {
    "detail": "Prompt not found"
  }
  ```

  or

  ```json
  {
    "detail": "Collection not found"
  }
  ```

- **Authentication:** None

### `DELETE /prompts/{prompt_id}`

- **Description:** Delete a prompt by its unique identifier.
- **Parameters:**
  - `prompt_id` (path): The unique identifier of the prompt.
- **Request Body:** None
- **Response:** 204 No Content
- **Error Responses:**

  ```json
  {
    "detail": "Prompt not found"
  }
  ```

- **Authentication:** None

## Collection Endpoints

### `GET /collections`

- **Description:** Retrieve a list of all collections.
- **Parameters:** None
- **Request Body:** None
- **Response:**

  ```json
  {
    "collections": [
      {
        "id": "string",
        "name": "string",
        "description": "string",
        "created_at": "2023-01-01T00:00:00Z",
        "updated_at": "2023-01-01T00:00:00Z"
      }
    ],
    "total": 1
  }
  ```

- **Error Responses:** None
- **Authentication:** None

### `GET /collections/{collection_id}`

- **Description:** Retrieve a collection by its unique identifier.
- **Parameters:**
  - `collection_id` (path): The unique identifier of the collection.
- **Request Body:** None
- **Response:**

  ```json
  {
    "id": "string",
    "name": "string",
    "description": "string",
    "created_at": "2023-01-01T00:00:00Z",
    "updated_at": "2023-01-01T00:00:00Z"
  }
  ```

- **Error Responses:**

  ```json
  {
    "detail": "Collection not found"
  }
  ```

- **Authentication:** None

### `POST /collections`

- **Description:** Create a new collection.
- **Parameters:** None
- **Request Body:**

  ```json
  {
    "name": "string",
    "description": "string"
  }
  ```

- **Response:**

  ```json
  {
    "id": "string",
    "name": "string",
    "description": "string",
    "created_at": "2023-01-01T00:00:00Z",
    "updated_at": "2023-01-01T00:00:00Z"
  }
  ```

- **Error Responses:** None
- **Authentication:** None

### `DELETE /collections/{collection_id}`

- **Description:** Delete a collection by its unique identifier.
- **Parameters:**
  - `collection_id` (path): The unique identifier of the collection.
- **Request Body:** None
- **Response:** 204 No Content
- **Error Responses:**

  ```json
  {
    "detail": "Collection not found"
  }
  ```

- **Note:** Prompts with this `collection_id` become orphaned.
- **Authentication:** None