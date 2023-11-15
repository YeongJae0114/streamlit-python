import requests
import base64
from PIL import Image
from io import BytesIO
import streamlit as st

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


else:
    print(f"Error: {response.status_code}")



for i in range(len(data_list)):
        car_dic ={
            'currentcar' : data_list[i]['currentcar'],
            'emptyspace' :  data_list[i]['emptyspace'],
            'totalspace' : data_list[i]['totalspace'],
        }
        car_data.append(car_dic)

print(car_data[0])