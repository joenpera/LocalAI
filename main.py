import sys
import ollama

# Initialize
try:
    client = ollama.Client()
except Exception as e:
    print("Error: ", e)
    print("Please check ollama server is running locally or give the correct IP address and port number")
    sys.exit(-1)

# Model name and prompt
model = "llama2" # 3.8GB model
prompt = """Create picture of a llama in a field with a mountain in the background. Use emojis and no text"""

# Query and response
print(f"prompt:    {prompt}")
response = client.generate(model=model, prompt=prompt)
print(f"response:  {response.response}")
