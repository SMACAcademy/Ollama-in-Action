from ollama import generate

#my-assistant:latest
#llama3.2
response_from_model = generate('my-assistant:latest', 'Why is the sky blue?')
print(response_from_model)

print("=========================================")

print(response_from_model['response'])