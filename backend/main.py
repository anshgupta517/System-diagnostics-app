from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import tool_router
import llm_service

app = FastAPI(title="AI System Summarizer")

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, replace with frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
async def root():
    return {"status": "System Summarizer Backend Running"}

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    user_msg = request.message
    
    # 1. Decide tools (Heuristic for now)
    # In Phase 2, LLM will decide this.
    tool_results = tool_router.router_tool_calls(user_msg)
    
    # 2. Generate response using Data + LLM
    response_text = await llm_service.query_llm(user_msg, tool_results)
    
    return {
        "response": response_text,
        "data_collected": tool_results # Sending raw data back might be useful for debug or UI badges
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
