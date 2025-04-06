# streamlit_app.py

import streamlit as st
from maintenance import faq

st.set_page_config(page_title="AutoCareBuddy 🚗", page_icon="🔧")
st.title("🔧 AutoCareBuddy: Your Car Maintenance Helper")
st.write("Ask me anything about car care! 🧰")

user_input = st.text_input("Type your question below:")

if user_input:
    user_question = user_input.lower().strip()

    found = False
    for key in faq:
        if key in user_question:
            st.success(faq[key])
            found = True
            break

    if not found:
        st.warning("Sorry, I don’t know that yet! Try asking about oil, tires, or check engine light.")
