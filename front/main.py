import os
import uuid
import requests
import streamlit as st
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

AGENT_URL = os.getenv("AGENT_URL", "http://localhost:8001")

st.set_page_config(page_title="건강검진 AI", page_icon="🩺")

# 세션 초기화
if "patient_id" not in st.session_state:
    st.session_state.patient_id = str(uuid.uuid4())
if "messages" not in st.session_state:
    st.session_state.messages = []


def fetch_models() -> list[str]:
    try:
        response = requests.get(f"{AGENT_URL}/chat/models", timeout=10, verify=False)
        response.raise_for_status()
        return response.json().get("models", [])
    except Exception:
        return ["llama3.1:8b", "qwen2.5:7b"]


# 헤더
st.title("🩺 건강검진 AI 어시스턴트")

# 환자 ID + 모델 선택
col1, col2, col3 = st.columns([4, 2, 1])
with col1:
    st.text_input("Patient ID", value=st.session_state.patient_id, disabled=True)
with col2:
    available_models = fetch_models()
    selected_model = st.selectbox("LLM 모델", available_models)
with col3:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄 새로 생성"):
        st.session_state.patient_id = str(uuid.uuid4())
        st.session_state.messages = []
        st.rerun()

st.divider()

# 대화 기록 렌더링
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        if msg["role"] == "assistant" and msg.get("model"):
            st.caption(f"모델: {msg['model']}")
        st.write(msg["content"])

# 채팅 입력
if prompt := st.chat_input("예: 최근 건강검진 결과는 어때요?"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        st.caption(f"모델: {selected_model}")
        full_response = ""
        placeholder = st.empty()

        try:
            with requests.post(
                f"{AGENT_URL}/chat/",
                json={
                    "patient_id": st.session_state.patient_id,
                    "question": prompt,
                    "model": selected_model,
                },
                stream=True,
                timeout=600,
                verify=False,
            ) as response:
                response.raise_for_status()
                for chunk in response.iter_content(chunk_size=None, decode_unicode=True):
                    full_response += chunk
                    placeholder.write(full_response + "▌")

            placeholder.write(full_response)
            st.session_state.messages.append({
                "role": "assistant",
                "content": full_response,
                "model": selected_model,
            })

        except Exception as e:
            error_msg = f"오류가 발생했습니다: {str(e)}"
            placeholder.error(error_msg)
            st.session_state.messages.append({
                "role": "assistant",
                "content": error_msg,
            })