import openai
import streamlit as st
from streamlit_chat import message
 
openai.api_key = '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'


st.header("🤖Leege's ChatGPT-3 (Demo)")
st.markdown("cilab")

# ChatGPT 모델과 관련한 설정
model_name = "gpt-3.5-turbo"

def generate_response(prompt):
    # ChatGPT를 사용하여 응답 생성
    response = openai.Completion.create(
        engine=model_name,
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

# Streamlit 앱 코드
def main():
    st.title("ChatGPT 연동 예제")
    st.write("ChatGPT와 대화해보세요!")

    # 사용자 입력 받기
    user_input = st.text_input("사용자 입력:")

    if user_input:
        # ChatGPT로부터 응답 생성
        response = generate_response(user_input)
        st.text_area("ChatGPT 응답:", value=response, height=200)

if __name__ == "__main__":
    main()
