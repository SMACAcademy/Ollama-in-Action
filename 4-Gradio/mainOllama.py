import ollama  


import gradio as gr

def query_ollama(prompt):
    response = ollama.chat(
        model="llama3.2",  
        messages=[
            #{"role": "user", "content": "Explain Embeddings and Vectors in AI."},  # User's input query
            {"role": "user", "content": prompt},  # User's input query
        ],
    )

    return response["message"]["content"]
    
    
# Call the Ollama model to generate a response  

interface = gr.Interface(fn=query_ollama, inputs="text", outputs="text")
#interface.launch()  # Set share to True to generate a public link
interface.launch(share=True)  # Set share to True to generate a public link
