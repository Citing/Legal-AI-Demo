import streamlit as st

# https://www.canva.com/colors/color-palettes/window-tide/
# Midnight Blue #41729f
# Blue Gray     #5885af
# Dark Blue     #274472
# Baby Blue     #c3e0e5


def set_layout():
    st.markdown("""
        <style>
            .stApp {
                background-color: #41729f;
            }

            .custom-header {
                font-size:50px;
                color: #c3e0e5;
                font-weight: bold;
                text-align: center;
                font-family: 'Helvetica', sans-serif;
            }

            .stTextInput>div>div>input {
                background-color: #274472;
                color: #aaaaaa;
                font-size: 18px;
            }

            .stButton>button {
                background-color: #5885af;
                color: #dddddd;
                font-size: 20px;
                border-radius: 10px;
            }

            .col-left {
                background-color: #5885af;
                color: black;
                font-size: 18px;
                padding: 10px;
            }
            .col-right {
                background-color: #c3e0e5;
                color: black;
                font-size: 18px;
                padding: 10px;
            }
        </style>
        """, 
        unsafe_allow_html=True
    )

    return

def write_left(text):
    st.markdown(f"<div class=\"col-left\">{text}</div>", unsafe_allow_html=True)
    return

def write_right(text):
    st.markdown(f"<div class=\"col-right\">{text}</div>", unsafe_allow_html=True)
    return