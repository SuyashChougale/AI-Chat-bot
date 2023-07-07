
import streamlit as st
from streamlit_message import message
import AI_based_bot


st.title("chatBot")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []

def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text
user_input = get_text()

if user_input:
    if user_input.lower() in ["quit","bye"]:
        output = AI_based_bot.quit(user_input)
    else:
        output = AI_based_bot.response(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)
    user_input = ""

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
