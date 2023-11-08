import streamlit as st 

# CSS 스타일을 정의하여 사이드바를 꾸밉니다.
st.sidebar.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #f2f2f2;
        padding: 20px;
        border-radius: 10px;
    }
    .sidebar .icon {
        color: #ff0000;
        font-size: 24px;
    }
    .sidebar .button-icon {
        color: #00ff00;
        font-size: 24px;
    }
    .sidebar .button-icon:hover {
        color: #0000ff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 버튼 및 아이콘을 추가한 꾸며진 사이드바
st.sidebar.title("Custom Sidebar")
page = "Home"

if st.sidebar.button("Home", key="home_button"):
    page = "Home"
    st.sidebar.markdown('<i class="icon bi-house"></i>', unsafe_allow_html=True)

if st.sidebar.button("About", key="about_button"):
    page = "About"
    st.sidebar.markdown('<i class="icon bi-info-circle"></i>', unsafe_allow_html=True)

if st.sidebar.button("Contact", key="contact_button"):
    page = "Contact"
    st.sidebar.markdown('<i class="icon bi-telephone"></i>', unsafe_allow_html=True)


if page == "Home":
    st.title("Home Page")
    st.write("Welcome to the Home Page!")

elif page == "About":
    st.title("About Page")
    st.write("This is the About Page. Here you can learn about us.")

elif page == "Contact":
    st.title("Contact Page")
    st.write("You can contact us at contact@example.com.")    