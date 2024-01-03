from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse, JSONResponse
from openai import OpenAI
import logging
app = FastAPI()

# Modify OpenAI's API key and API base to use the provided server.
openai_api_key = "EMPTY"
openai_api_base = "http://207.102.87.207:50503/"
client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)
logging.basicConfig(level=logging.DEBUG)

# Custom Middleware to log incoming requests
@app.middleware("http")
async def log_requests(request, call_next):
    logging.info(f"Incoming request: {request.method} {request.url}")
    response = await call_next(request)
    return response
    
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
