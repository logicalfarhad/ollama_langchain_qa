from fastapi import FastAPI, HTTPException
from langchain.llms import Ollama

app = FastAPI()

# Configuration
ollama_url = "http://ollama_chat:11434"  # Adjust URL as needed
ollama_model = "mistral"  # Adjust model name as needed

# Create an instance of Ollama
ollama_obj = Ollama(base_url=ollama_url, model=ollama_model)

# API endpoint for generating text based on a prompt
@app.get("/")
async def read_root():
    try:
        # Generate a message using Ollama
        message = ollama_obj.ask("Generate a message for the root route.")
        return {"message": message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api")
async def generate_text(prompt: str):
    try:
        # Generate text based on the prompt using the Mistral model
        generated_text = ollama_obj.ask(prompt)
        return {"generated_text": generated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
