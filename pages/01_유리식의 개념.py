import streamlit as st
import random

# 페이지 기본 설정
st.set_page_config(page_title="유리식 개념 학습기", page_icon="🧮")

st.title("🧮 유리식의 개념 학습 & 문제 생성기")
st.markdown("---")

# 유리식의 개념 설명
st.header("📘 유리식의 개념과 정의")

st.markdown("""
**유리식(有理式)**이란 **다항식과 다항식의 나눗셈으로 이루어진 식**을 말해요.  
즉, 분모와 분자가 모두 다항식(polynomial)인 식입니다.  
예를 들어,

- \\( \\frac{x+1}{x-2} \\)
- \\( \\frac{3x^2 - 2}{x^2 + 4x + 3} \\)

이런 식들을 유리식이라고 해요.  

단, **분모가 0이 되는 값은 정의되지 않는다**는 점이 중요합니다 ⚠️  
예를 들어 \\( \\frac{x+1}{x-2} \\) 는 \\(x = 2\\) 에서 정의되지 않아요.
""")

st.markdown("---")
st.header("🧩 유리식 관련 개념 문제 생성기")

# 문제 리스트
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
        "q": "유리식 \\( \\frac{x+2}{x-3} \\) 이 정의되지 않는 값은?",
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
        "q": "유리식 \\( \\frac{x² - 9}{x + 3} \\) 을 간단히 하면?",
        "choices": [
            "① x - 3", "② x + 3", "③ x² + 9", "④ x² - 3x"
        ],
        "answer": "① x - 3"
    }
]

# 문제 생성 버튼
if st.button("🔄 랜덤 문제 생성하기"):
    q = random.choice(questions)
    st.subheader("📖 문제")
    st.write(q["q"])
    st.write("\n".join(q["choices"]))
    st.markdown(" ")
    
    # 정답 확인용
    with st.expander("✅ 정답 보기"):
        st.write(q["answer"])
else:
    st.info("⬆️ 위 버튼을 눌러 랜덤 문제를 생성하세요!")

st.markdown("---")
st.caption("만든이: ChatGPT × 고등학생 코더 ✨")
