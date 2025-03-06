import streamlit as st
from openai import OpenAI


# Initialize the Ollama client
ollama_client = OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="not_used",  # required, but unused
    )


st.title('Ollama Text Generator')

# Text input from user
user_input = st.text_input("Enter your text here:")

# Button to generate text
if st.button('Generate'):

    response = ollama_client.chat.completions.create(
        model="llama3.2",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"},
            {"role": "assistant", "content": "The LA Dodgers won in 2020."},
            {"role": "user", "content": "Where was it played?"}
        ]
    )
    st.write(response.choices[0].message.content)
