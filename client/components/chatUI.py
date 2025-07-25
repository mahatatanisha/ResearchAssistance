import streamlit as st
from utils.api import ask_question

def render_chat():
    st.subheader("💬 Chat with your assistant")

    if "messages" not in st.session_state:
        st.session_state.messages=[]

        #render existing chat history
        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).markdown(msg["content"])

        # input and response
        user_input= st.chat_input("Type you question....")
        if user_input:
            st.chat_message("user").markdown(user_input)
            st.session_state.messages.append({"role":"user","content":user_input})

            response=ask_question(user_input)
            if response.status_code==200:
                data=response.json()
                answer=data["response"]
                sources=data.get("assistant")
                st.chat_message("assistant").markdown(answer)
                st.session_state.messages.append({"role":"assistant","content":answer})
            
            else:
                st.error(f"Error: {response.text}")