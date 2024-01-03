from interpreter import interpreter

interpreter.offline = True # Disables online features like Open Procedures
interpreter.llm.model = "openai/TheBloke/NeuralHermes-2.5-Mistral-7B-GPTQ" # Tells OI to send messages in OpenAI's format
#interpreter.llm.model = "openai/TheBloke/deepseek-coder-6.7B-instruct-GPTQ" # Tells OI to send messages in OpenAI's format
interpreter.llm.api_key = "EMPTY" # LiteLLM, which we use to talk to LM Studio, requires this
# interpreter.llm.api_base = "http://207.102.87.207:50503/v1" # Point this at any OpenAI compatible server
interpreter.llm.api_base = "https://aianyone.net/v1/chat/completion" # Point this at any OpenAI compatible server
interpreter.llm.auto_run = True
interpreter.llm.context_window = 100000
interpreter.llm.max_tokens = 100000
interpreter.chat()
