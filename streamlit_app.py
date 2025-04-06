# streamlit_app.py

import streamlit as st
from maintenance import faq
from datetime import datetime

st.set_page_config(page_title="AutoCare Bestie 💬🚗", page_icon="💖")

# Store name and date in session
if 'name' not in st.session_state:
    st.session_state.name = ""
if 'date' not in st.session_state:
    st.session_state.date = ""

# Welcome area
st.title("💖 AutoCare Bestie Chatbot")
st.write("Hey friend! I'm here to help with your car worries 🚗💬")

# Ask name
if st.session_state.name == "":
    name = st.text_input("First things first — what's your name? 🌸")
    if name:
        st.session_state.name = name
        st.rerun()

# Ask date
elif st.session_state.date == "":
    today = st.date_input(f"Nice to meet you, {st.session_state.name}! What's the date today? 📅")
    if today:
        st.session_state.date = today
        st.rerun()

# Main chatbot interface
else:
    st.success(f"Welcome back, {st.session_state.name}! Let's take care of your car today 🛠️")
    st.write("Choose a problem below or type your question!")

    # Display FAQ options as buttons
    for key in faq:
        if st.button(f"💬 {key.capitalize()}"):
            st.markdown(f"👩‍🔧 **AutoCare Bestie:** {faq[key]}")

    # Let user type questions too
    st.divider()
    st.subheader("Or type your question here 👇")

    user_input = st.text_input("Got a specific question?")
    if user_input:
        user_question = user_input.lower().strip()
        found = False
        for key in faq:
            if key in user_question:
                st.markdown(f"👩‍🔧 **AutoCare Bestie:** {faq[key]}")
                found = True
                break
        if not found:
            st.markdown("🤔 **AutoCare Bestie:** Hmm, I’m not sure about that one. Try picking from the list above! 💡")
