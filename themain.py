from interpreter import interpreter
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, StreamingResponse
from openai import OpenAI
import logging
import requests

yes = FastAPI()

interpreter.offline = True
interpreter.llm.model = "openai/TheBloke/NeuralHermes-2.5-Mistral-7B-GPTQ"
interpreter.llm.api_key = "EMPTY"
interpreter.llm.api_base = "http://207.102.87.207:50503/v1"
interpreter.auto_run = True

@yes.post("/send_message")
def send_message(data: dict):
    message = data.get("message")
    if not message:
        raise HTTPException(status_code=422, detail="Message is required")

    def event_stream():
        for result in interpreter.chat(message, stream=True):
            yield f"data: {result}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")

@yes.get("/history")
def history_endpoint():
    return interpreter.messages
