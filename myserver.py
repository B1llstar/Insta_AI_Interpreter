from interpreter import interpreter
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, StreamingResponse
from openai import OpenAI
import logging
import requests

app = FastAPI()
interpreter.offline = False
interpreter.llm.model = "openai/TheBloke/NeuralHermes-2.5-Mistral-7B-GPTQ"
interpreter.llm.api_key = "EMPTY"
interpreter.llm.api_base = "http://207.102.87.207:50503/v1"
interpreter.auto_run = False
openai_api_key = "EMPTY"
openai_api_base = "http://207.102.87.207:50503/v1"
client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)
logging.basicConfig(level=logging.DEBUG)

@app.middleware("http")
async def log_requests(request, call_next):
    logging.info(f"Incoming request: {request.method} {request.url}")
    response = await call_next(request)
    return response

@app.get("/chat")
def chat_endpoint(message: str):
    def event_stream():
        try:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {openai_api_key}",
            }
            
            data = {
                "model": "TheBloke/NeuralHermes-2.5-Mistral-7B-GPTQ",
                "messages": [
                    {"role": "system", "content": "Two days ago, Bill said: \"I love my steak cooked medium!\""},
                    {"role": "Bill", "content": "How do I like my steak cooked, assistant?"}
                ],
            }

            print(data)
            response = requests.post(
                f"http://207.102.87.207:50503/v1/chat/completions",  # Adjusted endpoint URL
                headers=headers,
                json=data,
            )
            
            response.raise_for_status()

            for chunk in response.iter_content(chunk_size=8192):
                # Log each chunk using the logger
                logging.debug(f"Received chunk: {chunk.decode('utf-8')}")

                yield f"data: {chunk.decode('utf-8')}\n\n"

        except requests.RequestException as e:
            logging.error(f"Error generating completion: {str(e)}")

    return StreamingResponse(event_stream(), media_type="text/event-stream")

@app.get("/history")
def history_endpoint():
    return interpreter.messages
