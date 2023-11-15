import streamlit as st
import requests
import base64
from PIL import Image
from io import BytesIO
from streamlit.components.v1 import html

# requests data
response = requests.get('http://43.200.254.150:8080/parking/')

url = "http://43.200.254.150:8080/parking/"  # 실제 API 엔드포인트로 교체해야 합니다.
img_endcode = []
car_data = []

# GET 요청 보내기
response = requests.get(url)
# 응답 코드 확인
if response.status_code == 200:
    # JSON 형식으로 응답 받기
    data_list = response.json()
    
    for i in range(1,4):
        data = (data_list[i]['image'])
        image_data = base64.b64decode(data)
        image = Image.open(BytesIO(image_data))
        img_endcode.append(image)

    for i in range(len(data_list)):
        car_dic ={
            'currentcar' : data_list[i]['currentcar'],
            'emptyspace' :  data_list[i]['emptyspace'],
            'totalspace' : data_list[i]['totalspace'],
        }
        car_data.append(car_dic)
 
else:
    print(f"Error: {response.status_code}")



# CSS 스타일
st.markdown(
    """
    <style>
    img {
        max-width: 100%; 
        height: auto; 
        max-height: 300px; 
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Define your javascript


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
            st.title(data_list[0]['parkingname'])
            st.image('img/n-7.jpeg')
            st.subheader('현재 차량 : {} '.format(data['currentcar']))
            st.subheader('남은 자리 : {}'.format(data['emptyspace']))
            st.subheader('총 주차공간 : {}'.format(data['totalspace']))

    elif page == "B":
        with container1:
            st.title(data_list[1]['parkingname'])
            st.image('img/test2.jpeg')
            st.text(data)
    elif page == "C":
        with container1:
            st.title(data_list[2]['parkingname'])
            st.image('img/test3.jpeg')
            st.text(data)
    elif page == "D":
        with container1:
            st.title(data_list[3]['parkingname'])
            st.image('img/test4.jpeg')
            st.text(data)


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
    st.header(data_list[0]['parkingname'])
    st.image('img/N-7_.jpeg')
    if st.button("주차장 현황"):
        page = "A"
        container1.empty()
        show_page(container1, page, car_data[0])
with col2:
    st.header(data_list[1]['parkingname'])
    st.image(img_endcode[1])
    if st.button("주차장 현황", key="B_button"):
        page = "B"
        container1.empty()
        show_page(container1, page, car_data[1])
with col3:
    st.header(data_list[2]['parkingname'])
    st.image(img_endcode[2])
    if st.button("주차장 현황", key="C_button"):
        page = "C"
        container1.empty()
        show_page(container1, page, car_data[2])
with col4:
    st.header(data_list[3]['parkingname'])
    st.image('img/s3.jpeg')
    if st.button("주차장 현황", key="D_button"):
        page = "D"
        container1.empty()
        show_page(container1, page, car_data[3])


