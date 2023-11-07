import streamlit as st
 
st.title('smart parking')

video = ['video/test4.mp4','video/test5.mp4']
# 탭 생성
tab_titles = ['A 주차장', 'B 주차장', 'C 주차장', 'D 주차장']
tab1, tab2, tab3, tab4 = st.tabs(tab_titles)


    
# 각 탭에 콘텐츠 추가
with tab1:
    st.header('A 주차장')
    st.video(video[0])
    st.write('주제 A의 내용')
 
with tab2:
    st.header('B 주차장')
    st.video(video[1])

with tab3:
    st.header('C 주차장')
    st.video(video[0])
    st.write('C의 내용')

with tab4:
    st.header('D 주차장')
    st.video(video[1])
    st.write('D의 내용')