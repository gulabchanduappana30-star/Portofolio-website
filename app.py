"""
FastAPI Backend for AI Portfolio.
Updated to securely handle API keys via environment variables.
"""

import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, EmailStr
from typing import List, Optional
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Access the key securely
API_KEY = os.getenv("")

app = FastAPI(title="AI Portfolio Backend", version="1.0.0")

# Safety check: Ensure API key is loaded
if not API_KEY:
    print("WARNING: API Key not found. Ensure .env file is configured.")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

class ContactMessage(BaseModel):
    name: str
    email: EmailStr
    subject: str
    message: str

class AIQuery(BaseModel):
    user_input: str
    session_id: Optional[str] = "default"

@app.get("/", response_class=HTMLResponse)
def read_root():
    """Serve the HTML frontend"""
    try:
        with open("templates/templates.html", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "<h1>Frontend not found. Ensure templates.html exists in the templates folder.</h1>"

@app.post("/contact")
async def receive_contact(contact: ContactMessage):
    try:
        print(f"New Message from {contact.name}: {contact.message}")
        return {"status": "success", "message": "Your message has been received."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/agent/query")
async def handle_agent_query(query: AIQuery):
    """
    Example of using the API_KEY within an agent call.
    """
    if not API_KEY:
        raise HTTPException(status_code=500, detail="AI Service not configured.")
        
    # Here you would use API_KEY with your LLM client (OpenAI, Anthropic, etc.)
    ai_response = f"Agent used secure key to process: '{query.user_input}'"
    
    return {
        "user_query": query.user_input,
        "agent_response": ai_response,
        "status": "completed"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
