# streamlit_app.py

import streamlit as st
from maintenance import faq

st.set_page_config(page_title="AutoCareBuddy 🚗", page_icon="🔧")

st.title("🔧 AutoCareBuddy: Your Car Maintenance Helper")
st.write("Ask me anything about car care!")

# Input from user
user_input = st.text_input("Type your question below:")

# Convert input to lowercase for matching
if user_input:
    user_question = user_input.lower().strip()

    # Look for a match in the FAQ
    answer = faq.get(user_question)

    if answer:
        st.success(answer)
    else:
        st.warning("Sorry, I don't know that yet! But I'm still learning. 😊")
        st.info("Try asking: *When should I change my oil?*, *How do I check tire pressure?*")
