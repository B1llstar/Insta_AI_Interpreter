from interpreter import interpreter

interpreter.offline = True # Disables online features like Open Procedures
interpreter.llm.model = "openai/x" # Tells OI to send messages in OpenAI's format
interpreter.llm.api_key = "EMPTY" # LiteLLM, which we use to talk to LM Studio, requires this
interpreter.llm.api_base = "http://207.102.87.207:50503/v1" # Point this at any OpenAI compatible server

interpreter.chat()
