"""PromptLab API Server

Run with: python main.py
"""

if __name__ == "__main__":
    import uvicorn
    # Use import string for reload to work
    uvicorn.run("app.api:app", host="0.0.0.0", port=8000, reload=True)