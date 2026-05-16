import streamlit as st
from groq import Groq

# Load API key from Streamlit Secrets
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

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
    # Add user message
    st.session_state.history.append({"role": "user", "content": user_input})

    # Get model response
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=st.session_state.history
    )

    bot_reply = response.choices[0].message.content

    # Add bot reply
    st.session_state.history.append({"role": "assistant", "content": bot_reply})

# Display conversation
for msg in st.session_state.history:
    if msg["role"] == "user":
        st.write("🧑 **You:**", msg["content"])
    else:
        st.write("🤖 **Bot:**", msg["content"])