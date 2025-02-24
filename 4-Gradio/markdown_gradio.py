import gradio as gr

def ask_question(uploaded_file, question):
    # Assuming 'ask_question' returns a Markdown formatted string
    markdown_response = f"**Question:** {question}\n**Answer:** This is a sample response in **bold**."
    return markdown_response

# Define a Gradio interface
interface = gr.Interface(
    fn=ask_question,  
    inputs=[
        gr.File(label="Upload PDF (optional)"),  
        gr.Textbox(label="Ask a question")  
    ],
    outputs=gr.Markdown(),  # Specify Markdown as the output type
    title="Ask Questions About Your PDF",
    description="Use this tool to ask questions about the uploaded PDF document. The response will be formatted using Markdown."
)

# Launch the Gradio interface to start the web-based app
interface.launch()
