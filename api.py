from fastapi import FastAPI, Request
from pydantic import BaseModel
from groq import Groq
import asyncio

app = FastAPI()

# Set your API key here
API_KEY = "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"
client = Groq(api_key=API_KEY)


class ChatRequest(BaseModel):
    messages: str

@app.post("/chat/llama3-8b")
async def chat_completions(request: ChatRequest):
    completion = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {
            "role": "user",
            "content": "{}".format(request.messages)
        },
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)
  
    response_text = ""
    for chunk in completion:
        response_text += chunk.choices[0].delta.content or ""
    
    return {"response": response_text}

@app.post("/chat/llama3-70b")
async def chat_completions(request: ChatRequest):
    completion = client.chat.completions.create(
    model= "llama3-70b-8192",
    messages=[
        {
            "role": "user",
            "content": "{}".format(request.messages)
        },
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)
  
    response_text = ""
    for chunk in completion:
        response_text += chunk.choices[0].delta.content or ""
    
    return {"response": response_text}


@app.post("/chat/gemma-7b")
async def chat_completions(request: ChatRequest):
    completion = client.chat.completions.create(
    model="gemma-7b-it",
    messages=[
        {
            "role": "user",
            "content": "{}".format(request.messages)
        },
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)
  
    response_text = ""
    for chunk in completion:
        response_text += chunk.choices[0].delta.content or ""
    
    return {"response": response_text}


@app.post("/chat/mixtral-7b")
async def chat_completions(request: ChatRequest):
    completion = client.chat.completions.create(
    model="mixtral-8x7b-32768",
    messages=[
        {
            "role": "user",
            "content": "{}".format(request.messages)
        },
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)
  
    response_text = ""
    for chunk in completion:
        response_text += chunk.choices[0].delta.content or ""
    
    return {"response": response_text}




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
