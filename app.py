import streamlit as st
import requests

# 🔴 API KEY
API_KEY = "nmngtEbbgaK8eR64H8Zt"

st.set_page_config(page_title="FDNC Checker")

st.title("📞 FDNC Number Checker")

phone = st.text_input("Enter Phone Number")

if st.button("Check"):
    if phone:
        with st.spinner("Checking..."):
            try:
                url = f"https://api.blacklistalliance.net/lookup?key={API_KEY}&ver=v3&resp=raw&phone={phone}"

                response = requests.get(url)
                data = response.text.strip()   # 👈 important

                st.success("Result Received")

                # 🔥 RESULT LOGIC
                if data == "1":
                    st.error("❌ FDNC Number (Blocked)")
                elif data == "0":
                    st.success("✅ Clean Number (Allowed)")
                else:
                    st.warning(f"Unknown Response: {data}")

            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Enter a number first")
