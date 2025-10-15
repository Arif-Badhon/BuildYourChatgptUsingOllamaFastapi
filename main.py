from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
from typing import List, Literal, Optional
import ollama
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Local LLM API (uv)")

Role = Literal["system", "user", "assistant"]

class Message(BaseModel):
    role: Role
    content: str

class ChatRequest(BaseModel):
    model: str = Field(default="gemma3:1b")
    messages: List[Message]
    stream: bool = Field(default=True)
    temperature: Optional[float] = 0.7
    top_p: Optional[float] = 0.9
    max_tokens: Optional[int] = None


app.mount("/static", StaticFiles(directory="static", html=True), name="static")



@app.post("/chat")
def chat(req: ChatRequest):
    try:
        if not req.stream:
            resp = ollama.chat(
                model=req.model,
                messages=[m.dict() for m in req.messages],
                options={
                    "temperature": req.temperature,
                    "top_p": req.top_p,
                    **({"num_predict": req.max_tokens} if req.max_tokens else {})
                },
                stream=False,
            )
            return {"content": resp["message"]["content"]}
        else:
            def token_stream():
                stream = ollama.chat(
                    model=req.model,
                    messages=[m.dict() for m in req.messages],
                    options={
                        "temperature": req.temperature,
                        "top_p": req.top_p,
                        **({"num_predict": req.max_tokens} if req.max_tokens else {})
                    },
                    stream=True,
                )
                for chunk in stream:
                    part = chunk.get("message", {}).get("content", "")
                    if part:
                        yield part
            return StreamingResponse(token_stream(), media_type="text/plain")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

