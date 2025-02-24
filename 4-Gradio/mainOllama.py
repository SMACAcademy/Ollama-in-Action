import gradio as gr
from OllamaClient import OllamaClient  # Replace 'your_module_name' with the actual name of your Python file without the .py extension

def query_ollama(prompt):
    ollama_client = OllamaClient()
    response = ollama_client.query(prompt)
    return response

interface = gr.Interface(fn=query_ollama, inputs="text", outputs="text")
interface.launch(share="True")  # Set share to True to generate a public link
