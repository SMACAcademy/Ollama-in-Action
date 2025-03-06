import streamlit as st
from openai import OpenAI

st.title("🦜🔗 Langchain Quickstart App")

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"


def generate_response(input_text):
    #llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    ollama_client = OpenAI(
            base_url="http://localhost:11434/v1",
            api_key="not_used",  # required, but unused
        )    
    response = ollama_client.chat.completions.create(
        model="llama3.2",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": input_text}
        ]
    )
    st.info(response.choices[0].message.content)


with st.form("my_form"):
    text = st.text_area("Enter text:", "What are 3 key advice for learning how to code?")
    submitted = st.form_submit_button("Submit")
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
    elif submitted:
        generate_response(text)