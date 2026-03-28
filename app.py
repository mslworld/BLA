import streamlit as st
import requests

# 🔴 APNI API DETAILS YAHA DALNI HAIN
API_URL = "https://api.blacklistalliance.net/lookup?key=nmngtEbbgaK8eR64H8Zt&ver=v3&resp=raw&phone=--A--phone_number--B--"
API_KEY = "nmngtEbbgaK8eR64H8Zt"

st.set_page_config(page_title="FDNC Checker")

st.title("📞 FDNC Number Checker")

phone = st.text_input("Enter Phone Number")

if st.button("Check"):
    if phone:
        with st.spinner("Checking..."):
            try:
                response = requests.post(
                    API_URL,
                    json={"phone": phone},
                    headers={
                        "Authorization": f"Bearer {API_KEY}",
                        "Content-Type": "application/json"
                    }
                )

                data = response.json()

                st.success("Result Received")

                # 👇 RAW RESULT
                st.json(data)

                # 👇 OPTIONAL (agar FDNC field ho)
                if "fdnc" in data:
                    if data["fdnc"]:
                        st.error("❌ FDNC Number")
                    else:
                        st.success("✅ Not FDNC")

            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Enter a number first")