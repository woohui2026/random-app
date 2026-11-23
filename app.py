import random
import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="오늘의 점심 추천기", page_icon="🍱")

st.title("🍱 오늘의 점심 메뉴 추천기")
st.write("무엇을 먹을지 고민될 때 아래 버튼을 눌러보세요!")

# 점심 메뉴 리스트 (원하는 메뉴를 자유롭게 추가/수정할 수 있습니다)
lunch_menus = [
    "김치찌개",
    "된장찌개",
    "제육볶음",
    "돈가스",
    "비빔밥",
    "칼국수",
    "짜장면",
    "짬뽕",
    "초밥",
    "쌀국수",
    "햄버거",
    "파스타",
    "국밥",
    "마라탕",
    "샌드위치",
    "떡볶이",
]

# 추천 버튼 생성
if st.button("🎲 오늘의 메뉴 추천받기", use_container_width=True):
    # random.choice()를 이용해 리스트에서 무작위로 하나 선택
    selected_menu = random.choice(lunch_menus)

    st.success(f"오늘의 추천 메뉴는 **{selected_menu}**입니다! 맛있게 드세요! 😋")
