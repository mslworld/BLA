from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()

# CORS (important for frontend connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔴 YAHAN APNI API DETAILS DALO
API_URL = "https://api.blacklistalliance.net/lookup?key=nmngtEbbgaK8eR64H8Zt&ver=v3&resp=raw&phone=--A--phone_number--B--"
API_KEY = "nmngtEbbgaK8eR64H8Zt"

class PhoneRequest(BaseModel):
    phone: str

@app.post("/check")
def check_number(data: PhoneRequest):
    try:
        response = requests.post(
            API_URL,
            json={"phone": data.phone},
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            }
        )

        result = response.json()

        return {
            "success": True,
            "result": result
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
