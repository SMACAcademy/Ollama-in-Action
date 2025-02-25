import gradio as gr

gr.load_chat("http://localhost:11434/v1/", model="llama3.2", token="***").launch(share=True)  # Set share to True to generate a public link
#gr.load_chat("http://localhost:11434/v1/", model="llama3.2", token="***").launch()  # Set share to True to generate a public link