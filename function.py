import streamlit as st
from streamlit.components.v1 import html

# Define your JavaScript for scrolling to the top
scroll_to_top_js = """
window.scrollTo(0, 0);
"""

# Wrap the JavaScript code as HTML
scroll_to_top_html = f"<script>{scroll_to_top_js}</script>"

# Function to scroll to the top of the page
def scroll_to_top():
    html(scroll_to_top_html)

def show_page(container1, page, data):
    scroll_to_top()  # Scroll to the top of the page
    if page == 'A':
        with container1:
            st.title("A 주차장")
            st.image('img/test1.jpeg')
            st.write(data)
    elif page == "B":
        with container1:
            st.title("B 주차장")
            st.image('img/test2.jpeg')
            st.write(data)
    elif page == "C":
        with container1:
            st.title("C 주차장")
            st.image('img/test3.jpeg')
            st.write(data)
    elif page == "D":
        with container1:
            st.title("D 주차장")
            st.image('img/test4.jpeg')
            st.write(data)
