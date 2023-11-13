import streamlit as st
from function import show_page
import requests
import base64
from PIL import Image
from io import BytesIO

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
    
    for i in range(len(data_list)):
        data = (data_list[i]['image'])
        car1 = '현재 차량 : ', data_list[i]['currentcar'] , '남은 주차 자리 ',data_list[i]['emptyspace'] , '총 주차 자리' ,data_list[i]['totalspace']
        image_data = base64.b64decode(data)
        image = Image.open(BytesIO(image_data))
        img_endcode.append(image)
        car_data.append(car1)
else:
    print(f"Error: {response.status_code}")
 


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
    st.header(data_list[0]['parkingname'])
    st.image(img_endcode[0])
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
    st.image(img_endcode[3])
    if st.button("주차장 현황", key="D_button"):
        page = "D"
        container1.empty()
        show_page(container1, page, car_data[3])
