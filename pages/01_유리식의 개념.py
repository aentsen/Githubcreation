import streamlit as st
import random

# 페이지 기본 설정
st.set_page_config(page_title="유리식 학습기", page_icon="📘")

# 제목
st.title("📘 유리식의 개념 학습 & 문제 생성기")
st.write("---")

# 🌟 개념 설명
st.header("1️⃣ 유리식의 개념과 정의")

st.markdown("""
**유리식(有理式)**이란 **두 다항식의 나눗셈으로 이루어진 식**을 말합니다.  
즉, **분자와 분모가 모두 다항식인 식**이에요.

예시로 보면:
- (x + 1) / (x - 2)
- (3x² - 2) / (x² + 4x + 3)

이런 식들이 전부 **유리식**이에요.  

⚠️ 단, **분모가 0이 되는 값은 정의되지 않는다!**
예를 들어, (x + 1) / (x - 2) 는 x = 2 에서 정의되지 않아요.
""")

st.write("---")

# 🌟 랜덤 문제 생성
st.header("2️⃣ 유리식 개념 문제 생성기")

questions = [
    {
        "q": "다음 중 유리식이 아닌 것은?",
        "choices": [
            "① (x + 1) / (x - 2)",
            "② (3x² - 1) / (x + 4)",
            "③ x² + 2x + 1",
            "④ (x³ + 2) / (x² + 1)"
        ],
        "answer": "③ x² + 2x + 1"
    },
    {
        "q": "유리식 (x + 2) / (x - 3) 이 정의되지 않는 값은?",
        "choices": [
            "① x = 3", "② x = -2", "③ x = 0", "④ x = 1"
        ],
        "answer": "① x = 3"
    },
    {
        "q": "다음 중 분모가 다항식이 아닌 것은?",
        "choices": [
            "① (x² + 1) / (x + 2)",
            "② (x + 1) / √x",
            "③ (x³ - 2) / (x² + 3x)",
            "④ (x - 5) / (x² - 4)"
        ],
        "answer": "② (x + 1) / √x"
    },
    {
        "q": "유리식 (x² - 9) / (x + 3) 을 간단히 하면?",
        "choices": [
            "① x - 3", "② x + 3", "③ x² + 9", "④ x² - 3x"
        ],
        "answer": "① x - 3"
    }
]

# 문제 생성 버튼
if st.button("🎲 랜덤 문제 생성"):
    q = random.choice(questions)
    st.subheader("📖 문제")
    st.markdown(q["q"])
    
    user_answer = st.radio("정답을 선택하세요:", q["choices"])
    
    if st.button("✅ 정답 확인"):
        if user_answer == q["answer"]:
            st.success("🎉 정답입니다!")
        else:
            st.error(f"❌ 오답입니다. 정답은 **{q['answer']}** 입니다.")
else:
    st.info("⬆️ 위 버튼을 눌러 문제를 생성하세요!")

st.write("---")
st.caption("© 2025 고등학생 코더 × ChatGPT - Streamlit 학습 프로젝트")
