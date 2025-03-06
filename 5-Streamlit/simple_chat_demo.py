import streamlit as st
import ollama

# Configuration for Ollama might involve setting up a base URL or similar parameters,
# ensure you adjust these settings based on your actual Ollama setup.
ollama_base_url = 'http://localhost:11434'  # Example URL, change it according to your setup
ollama_model = 'llama3.2:latest'  # Change according to the model you are using

st.title("💬 Chatbot")
st.caption("🚀 A Streamlit chatbot powered by Ollama")

# Initialize the Ollama client - assuming a similar setup to your previous descriptions
ollama_client = ollama.Ollama(ollama_model, base_url=ollama_base_url)

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Assuming Ollama uses a function similar to 'chat' to handle message generation
    # and that it accepts a list of previous messages to maintain context.
    response = ollama_client.chat(prompt=prompt, past_messages=st.session_state["messages"])
    
    # Assuming the response from Ollama is direct and does not require parsing like OpenAI's structure.
    msg = response['content']  # Adjust based on how Ollama structures its response
    st.session_state["messages"].append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
