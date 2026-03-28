import streamlit as st
import requests

# 🔴 APNI API KEY YAHAN DALO
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

                # 🔴 TEXT response (important)
                data = response.text

                st.success("Result Received")

                # 👇 RAW RESULT
                st.code(data)

            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Enter a number first")