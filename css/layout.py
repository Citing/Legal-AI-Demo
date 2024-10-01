import streamlit as st

# https://www.canva.com/colors/color-palettes/window-tide/
# Midnight Blue #41729f
# Blue Gray     #5885af
# Dark Blue     #274472
# Baby Blue     #c3e0e5

# https://www.canva.com/colors/color-palettes/speckled-eggs/
# Baby Blue     #bfd7ed
# Blue Grotto   #60a3d9
# Royal Blue    #0074b7
# Navy Blue     #003b73

css = """
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

        .stTextArea [data-baseweb=base-input] {
            background-color: #274472;
            color: #274472;
            font-size: 16px;
        }

        .stFileUploader [data-testid=stFileUploaderDropzone] {
            background-color: #60a3d9;
            font-size: 16px;
        }

        .stTextInput>div>div>input {
            background-color: #274472;
            color: #aaaaaa;
            font-size: 18px;
        }

        .stButton>button {
            background-color: #274472;
            color: #dddddd;
            font-size: 20px;
            border-radius: 10px;
        }

        .col-left {
            background-color: #0074b7;
            color: black;
            font-size: 18px;
            padding: 10px;
        }
        .col-right {
            background-color: #60a3d9;
            color: black;
            font-size: 18px;
            padding: 10px;
        }
    </style>
"""

def set_layout():
    st.markdown(css, unsafe_allow_html=True)
    return

def write_left(text):
    st.markdown(f"<div class=\"col-left\">{text}</div>", unsafe_allow_html=True)
    return

def write_right(text):
    st.markdown(f"<div class=\"col-right\">{text}</div>", unsafe_allow_html=True)
    return

def set_header(header):
    st.markdown(f"<h1 class=\"custom-header\">{header}</h1>", unsafe_allow_html=True)
    return
