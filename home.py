import streamlit as st
import pandas as pd

st.write("### Button")
b_col1, b_col2, _, _, _ = st.columns(5)
with b_col1:
    st.button("Button")
with b_col2:
    st.button("Primary", type="primary")
    
st.write("### Columns")
col1, col2, col3 = st.columns(3)
with col1:
    st.write("#### A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.write("#### A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.write("#### An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")

st.write("### Form")
with st.form(key='my_form'):
    text_input = st.text_input(label='Enter some text')
    submit_button = st.form_submit_button(label='Submit')

st.write("### Table")
data = {'이름': ['홍길동', '김철수', '이영희'],
        '나이': [30, 25, 35],
        '성별': ['남자', '남자', '여자']}
 
df = pd.DataFrame(data)
 
st.table(df)

st.write("### Checkbox")
if st.checkbox('자세한 내용 보기'):
    st.write("자세한 내용")
    
st.write("### Text Input")
title = st.text_input('입력 값 : ', 'Default Text')
st.write('현재 입력값은 :', title)

st.write("### Multi Select")
options = st.multiselect(
    '오늘의 점심 메뉴는?',
    ['짜장면', '탕수육', '김밥', '샐러드'],
    ['짜장면', '김밥']
)
st.write('선택한 메뉴:', options)

st.write("### Container")
container = st.container(border=True)
container.write("컨테이너 안쪽 입니다!")
st.write("컨테이너 바깥쪽 입니다!")

st.write("### Tab")
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])


with tab1:
   st.write("#### A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)