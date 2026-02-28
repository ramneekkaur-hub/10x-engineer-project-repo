from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

from app.models import (
    Prompt, PromptCreate, PromptUpdate,
    Collection, CollectionCreate,
    PromptList, CollectionList, HealthResponse,
    get_current_time
)
from app.storage import storage
from app.utils import sort_prompts_by_date, filter_prompts_by_collection, search_prompts
from app import __version__

app = FastAPI(
    title="PromptLab API",
    description="AI Prompt Engineering Platform",
    version=__version__
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============== Health Check ==============

@app.get("/health", response_model=HealthResponse)
def health_check():
    """Check the health status of the API.
    
    Returns:
        HealthResponse: Object containing status and version information.
    """
    return HealthResponse(status="healthy", version=__version__)


# ============== Prompt Endpoints ==============

@app.get("/prompts", response_model=PromptList)
def list_prompts(
    collection_id: Optional[str] = None,
    search: Optional[str] = None
):
    """Retrieve a list of all prompts with optional filtering and search.
    
    Returns:
        PromptList: Object containing list of prompts and total count.
    """
    prompts = storage.get_all_prompts()
    
    # Filter by collection if specified
    if collection_id:
        prompts = filter_prompts_by_collection(prompts, collection_id)
    
    # Search if query provided
    if search:
        prompts = search_prompts(prompts, search)
    
    # Note: Sorting functionality is corrected here
    # Sort by descending date to get the newest prompts first
    prompts = sort_prompts_by_date(prompts)[::-1]
    
    return PromptList(prompts=prompts, total=len(prompts))


def validate_collection(collection_id: Optional[str]):
    """Helper function to validate collection existence.

    Args:
        collection_id: The ID of the collection to validate.

    Raises:
        HTTPException: 400 error if collection does not exist.
    """
    if collection_id:
        collection = storage.get_collection(collection_id)
        if not collection:
            raise HTTPException(status_code=400, detail="Collection not found")


@app.get("/prompts/{prompt_id}", response_model=Prompt)
def get_prompt(prompt_id: str):
    """Retrieve a prompt by its unique identifier.
    
    Returns:
        Prompt: The prompt object if found.
        
    Raises:
        HTTPException: 404 error if prompt is not found.
    """
    prompt = storage.get_prompt(prompt_id)
    if not prompt:
        raise HTTPException(status_code=404, detail="Prompt not found")
    return prompt


@app.post("/prompts", response_model=Prompt, status_code=201)
def create_prompt(prompt_data: PromptCreate):
    """Create a new prompt.
    
    Returns:
        Prompt: The newly created prompt object.
        
    Raises:
        HTTPException: 400 error if the specified collection does not exist.
    """
    # Validate collection exists if provided
    validate_collection(prompt_data.collection_id)
    
    prompt = Prompt(**prompt_data.model_dump())
    return storage.create_prompt(prompt)


@app.put("/prompts/{prompt_id}", response_model=Prompt)
def update_prompt(prompt_id: str, prompt_data: PromptUpdate):
    """Update an entire prompt with new data.
    
    Returns:
        Prompt: The updated prompt object.
        
    Raises:
        HTTPException: 404 error if prompt is not found.
    """
    existing = storage.get_prompt(prompt_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Prompt not found")
    
    # Validate collection if provided
    validate_collection(prompt_data.collection_id)
    
    # Update the prompt with new data and current timestamp
    updated_prompt = Prompt(
        id=existing.id,
        title=prompt_data.title,
        content=prompt_data.content,
        description=prompt_data.description,
        collection_id=prompt_data.collection_id,
        created_at=existing.created_at,
        updated_at=get_current_time()
    )
    
    return storage.update_prompt(prompt_id, updated_prompt)


@app.patch("/prompts/{prompt_id}", response_model=Prompt)
def patch_prompt(prompt_id: str, prompt_data: PromptUpdate):
    """Partially update a prompt with only provided fields.
    
    Returns:
        Prompt: The updated prompt object.
        
    Raises:
        HTTPException: 404 error if prompt is not found.
    """
    existing = storage.get_prompt(prompt_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Prompt not found")
    
    # Validate collection if provided
    validate_collection(prompt_data.collection_id)
    
    # Update only provided fields
    update_data = prompt_data.model_dump(exclude_unset=True)
    updated_prompt = existing.model_copy(update={
        **update_data,
        "updated_at": get_current_time()
    })
    
    return storage.update_prompt(prompt_id, updated_prompt)


@app.delete("/prompts/{prompt_id}", status_code=204)
def delete_prompt(prompt_id: str):
    """Delete a prompt by its unique identifier.
    
    Raises:
        HTTPException: 404 error if prompt is not found.
    """
    if not storage.delete_prompt(prompt_id):
        raise HTTPException(status_code=404, detail="Prompt not found")
    return None


# ============== Collection Endpoints ==============

@app.get("/collections", response_model=CollectionList)
def list_collections():
    """Retrieve a list of all collections.
    
    Returns:
        CollectionList: Object containing list of collections and total count.
    """
    collections = storage.get_all_collections()
    return CollectionList(collections=collections, total=len(collections))


@app.get("/collections/{collection_id}", response_model=Collection)
def get_collection(collection_id: str):
    """Retrieve a collection by its unique identifier.
    
    Returns:
        Collection: The collection object if found.
        
    Raises:
        HTTPException: 404 error if collection is not found.
    """
    collection = storage.get_collection(collection_id)
    if not collection:
        raise HTTPException(status_code=404, detail="Collection not found")
    return collection


@app.post("/collections", response_model=Collection, status_code=201)
def create_collection(collection_data: CollectionCreate):
    """Create a new collection.
    
    Returns:
        Collection: The newly created collection object.
    """
    collection = Collection(**collection_data.model_dump())
    return storage.create_collection(collection)


@app.delete("/collections/{collection_id}", status_code=204)
def delete_collection(collection_id: str):
    """Delete a collection by its unique identifier.
        
    Raises:
        HTTPException: 404 error if collection is not found.
    """
    if not storage.delete_collection(collection_id):
        raise HTTPException(status_code=404, detail="Collection not found")
    
    # Handle prompts that belong to this collection
    prompts = storage.get_prompts_by_collection(collection_id)
    for prompt in prompts:
        storage.delete_prompt(prompt.id)
    
    return None
