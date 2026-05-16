import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Streamlit UI
st.title("🧠 Multi-Turn Chatbot with Memory (Groq + Streamlit)")

# Initialize session memory
if "history" not in st.session_state:
    st.session_state.history = []

# Reset button
if st.button("Reset Chat"):
    st.session_state.history = []
    st.success("Chat history cleared!")

# User input
user_input = st.text_input("You:", "")

if user_input:
    # Add user message to memory
    st.session_state.history.append({"role": "user", "content": user_input})

    # Prepare model response
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=st.session_state.history
    )

    bot_reply = response.choices[0].message.content

    # Add assistant message to memory
    st.session_state.history.append({"role": "assistant", "content": bot_reply})

# Display conversation nicely
for msg in st.session_state.history:
    if msg["role"] == "user":
        st.write("🧑 **You:** " + msg["content"])
    else:
        st.write("🤖 **Bot:** " + msg["content"])