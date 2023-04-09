from fastapi import FastAPI, Request
import requests
import json
from fastapi.middleware.cors import CORSMiddleware
import logging

app = FastAPI()

# Handling Cors Error
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/send-slack-message")
async def root(request: Request):
    try:
        url = #YOUR WEBHOOK URL
        
        msg = await request.json()
        msg = msg['message']
        
        data = {
            "text": msg
        }
        
        json_payload = json.dumps(data)

        resp = requests.post(url, data=json_payload)
        resp_data = resp.json()
        logging.info("Message has been sent successfully..")
        
    except Exception as e:
        logging.error(f"Message operation failed -> {e}")
    return 
