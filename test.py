import streamlit as st
from function import show_page

# CSS 스타일
st.markdown(
    """
    <style>
    img {
        max-width: 100%; 
        height: auto; 
        max-height: 400px; 
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Define your javascript


container1 = st.container()
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
page = "Home"

# 사이드바
st.sidebar.title("Custom Sidebar")
# 페이지를 나타내는 버튼 추가
if st.sidebar.button("Home"):
    page = "Home"

with col1:
    st.header("Col1")
    st.image("https://static.streamlit.io/examples/cat.jpg")
    if st.button("A"):
        page = "A"
        container1.empty()
        show_page(container1, page)
with col2:
    st.header("Col2")
    st.image("https://static.streamlit.io/examples/dog.jpg")
    if st.button("B", key="B_button"):
        page = "B"
        container1.empty()
        show_page(container1, page)
with col3:
    st.header("Col3")
    st.image("https://static.streamlit.io/examples/cat.jpg")
    if st.button("C", key="C_button"):
        page = "C"
        container1.empty()
        show_page(container1, page)
with col4:
    st.header("Col4")
    st.image("https://static.streamlit.io/examples/dog.jpg")
    if st.button("D", key="D_button"):
        page = "D"
        container1.empty()
        show_page(container1, page)


