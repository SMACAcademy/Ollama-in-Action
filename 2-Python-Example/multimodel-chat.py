from ollama import chat

# from pathlib import Path

# Pass in the path to the image
# .\2-Python-Example\1995079_1280.jpg
path = input('Please enter the path to the image: ')

# You can also pass in base64 encoded image data
# img = base64.b64encode(Path(path).read_bytes()).decode()
# or the raw bytes
# img = Path(path).read_bytes()

response = chat(
  model='llama3.2-vision',
  messages=[
    {
      'role': 'user',
      'content': 'What is in this image? Be concise.',
      'images': [path],
    }
  ],
)

print(response.message.content)