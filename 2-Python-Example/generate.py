from ollama import generate


response_from_model = generate('llama3.2', 'Why is the sky blue?')
print(response_from_model)

print("=========================================")

print(response_from_model['response'])