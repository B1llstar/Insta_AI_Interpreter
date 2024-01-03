from interpreter import interpreter
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse, JSONResponse
from openai import OpenAI
import logging
app = FastAPI()

interpreter.offline = False # Disables online features like Open Procedures
interpreter.llm.model = "openai/TheBloke/NeuralHermes-2.5-Mistral-7B-GPTQ" # Tells OI to send messages in OpenAI's format
#interpreter.llm.model = "openai/TheBloke/deepseek-coder-6.7B-instruct-GPTQ" # Tells OI to send messages in OpenAI's format
interpreter.llm.api_key = "EMPTY" # LiteLLM, which we use to talk to LM Studio, requires this
# interpreter.llm.api_base = "http://207.102.87.207:50503/v1" # Point this at any OpenAI compatible server
interpreter.llm.api_base = "https://aianyone.net/v1/chat/completion" # Point this at any OpenAI compatible server
interpreter.auto_run = True
interpreter.chat()

@app.get("/chat")
def chat_endpoint(message: str):
    print('Going')
    try:
        completion_result = client.completions.create(
            model="TheBloke/NeuralHermes-2.5-Mistral-7B-GPTQ",
            prompt=message,
        )
    except Exception as e:
        logging.error(f"Error generating completion: {str(e)}")    
        raise HTTPException(status_code=500, detail=f"Error generating completion: {str(e)}")

    return JSONResponse(content={"data": completion_result.get("choices")[0].get("text")})

@app.get("/history")
def history_endpoint():
    # Assuming interpreter.messages is a list of messages
    return JSONResponse(content={"history": interpreter.messages})
    
