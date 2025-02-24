import requests
import json
import gradio as gr

# Ollama API setup
url = 'http://localhost:11434/api/generate'  # Adjust if needed based on your specific endpoint
headers = {'Content-Type': 'application/json'}

def call_ollama(prompt):
    # Data to send to Ollama, adjust the structure according to your Ollama API requirements
    data = {
        'model': 'llama3.2',  # Specify your model version
        'prompt': prompt,
        'options': {
            'top_k': 40,
            'temperature': 0.8,
            'top_p': 0.9
        }
    }

    # POST request to the Ollama API
    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()  # To handle HTTP errors

    # Parsing the JSON response
    response_data = response.json()
    return response_data.get('text', "No response text found.")  # Change key as per your API response

# Gradio Interface
def setup_gradio_interface():
    with gr.Blocks() as app:
        with gr.Row():
            prompt_input = gr.Textbox(label="Enter your prompt:")
            submit_button = gr.Button("Generate")
        output = gr.Textbox(label="Ollama Response", readonly=True)

        submit_button.click(
            fn=call_ollama,
            inputs=prompt_input,
            outputs=output
        )

    return app

# Launch Gradio app
app = setup_gradio_interface()
app.launch()
