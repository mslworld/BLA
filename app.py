import streamlit as st
import requests

# 🔴 API KEY
API_KEY = "nmngt64H8Zt"

# 🔥 Page Config
st.set_page_config(page_title="FDNC Checker", layout="centered")

# 🔥 Custom CSS (PRO UI)
st.markdown("""
    <style>
    body {
        background-color: #0e1117;
    }
    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .result-box {
        text-align: center;
        font-size: 28px;
        padding: 20px;
        border-radius: 15px;
        margin-top: 20px;
        font-weight: bold;
    }
    .green {
        background-color: #0f5132;
        color: #d1e7dd;
    }
    .red {
        background-color: #842029;
        color: #f8d7da;
    }
    .input-box {
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# 🔥 Title
st.markdown('<div class="main-title">📞 FDNC Number Checker</div>', unsafe_allow_html=True)

# 🔥 Input
phone = st.text_input("Enter Phone Number", placeholder="e.g. 9402120565")

# 🔥 Button Center
col1, col2, col3 = st.columns([1,2,1])
with col2:
    check = st.button("Check Number")

# 🔥 Logic
if check:
    if phone:
        with st.spinner("Checking..."):
            try:
                url = f"https://api.blacklistalliance.net/lookup?key={API_KEY}&ver=v3&resp=raw&phone={phone}"
                response = requests.get(url)
                data = response.text.strip()

                # 🔥 RESULT DISPLAY
                if data == "1":
                    st.markdown(
                        '<div class="result-box red">❌ FDNC NUMBER<br>BLOCKED</div>',
                        unsafe_allow_html=True
                    )

                elif data == "0":
                    st.markdown(
                        '<div class="result-box green">✅ CLEAN NUMBER<br>ALLOWED</div>',
                        unsafe_allow_html=True
                    )

                else:
                    st.warning(f"Unknown Response: {data}")

            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Enter a number first")
