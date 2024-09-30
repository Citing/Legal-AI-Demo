import streamlit as st
from utils.ai import chat
from css.layout import set_layout

set_layout()

st.markdown('<h1 class="custom-header">Legal AI Demo</h1>', unsafe_allow_html=True)


if 'prompts' not in st.session_state:
    st.session_state['prompts'] = [{"role": "system", "content": "You are a legal specialist"}]

question = st.text_input(label="Your Question:", label_visibility="hidden", placeholder="Message LegalGPT")

if st.button("Ask"):
    st.session_state['prompts'].append({"role": "user", "content": question})
    answer = chat(st.session_state['prompts'])
    st.session_state['prompts'].append({"role": "assistant", "content": answer})

for i, prompt in enumerate(st.session_state['prompts'][1:]):
    col1, col2 = st.columns([2, 8])
    if prompt['role'] == 'user':
        with col1:
            st.markdown(f"<div class=\"col-left\">{prompt['content']}</div>", unsafe_allow_html=True)
    elif prompt['role'] == 'assistant':
        with col2:
            st.markdown(f"<div class=\"col-right\">{prompt['content']}</div>", unsafe_allow_html=True)
    

