import streamlit as st
import random

# 🎨 기본 설정
st.set_page_config(page_title="가위✌️ 바위✊ 보✋ 게임", page_icon="🎮", layout="centered")

# 🎉 타이틀 및 헤더
st.markdown("""
# 🎮 가위✌️ 바위✊ 보✋ 챌린지!
### 🤖 컴퓨터를 상대로 이겨보세요! 운이 좋으신가요? 🍀
""")

# 🎭 이모지 매핑
choices = {
    "가위": "✌️",
    "바위": "✊",
    "보": "✋"
}

# 🎮 사용자 선택
st.markdown("## 당신의 선택은? 🧐")
col1, col2, col3 = st.columns(3)

user_choice = None
with col1:
    if st.button("✌️ 가위"):
        user_choice = "가위"
with col2:
    if st.button("✊ 바위"):
        user_choice = "바위"
with col3:
    if st.button("✋ 보"):
        user_choice = "보"

# 👾 컴퓨터 선택 및 결과 계산
if user_choice:
    computer_choice = random.choice(list(choices.keys()))

    st.markdown("---")
    st.markdown("## 🆚 대결 결과")
    
    col_user, col_vs, col_computer = st.columns([2, 1, 2])
    with col_user:
        st.markdown(f"**당신**<br>{choices[user_choice]}", unsafe_allow_html=True)
    with col_vs:
        st.markdown("<h2 style='text-align:center;'>VS</h2>", unsafe_allow_html=True)
    with col_computer:
        st.markdown(f"**컴퓨터**<br>{choices[computer_choice]}", unsafe_allow_html=True)

    result = ""
    if user_choice == computer_choice:
        result = "😲 무승부입니다!"
    elif (
        (user_choice == "가위" and computer_choice == "보") or
        (user_choice == "바위" and computer_choice == "가위") or
        (user_choice == "보" and computer_choice == "바위")
    ):
        result = "🎉 당신이 이겼습니다! 멋져요! 👏"
    else:
        result = "😢 아쉽네요! 컴퓨터가 이겼어요..."

    st.markdown(f"""
    <div style='font-size:24px; text-align:center; margin-top:20px;'>
        {result}
    </div>
    """, unsafe_allow_html=
