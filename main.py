import os

from streamlit_webrtc import webrtc_streamer
from twilio.rest import Client

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

token = client.tokens.create()

webrtc_streamer(
    key="sample",
    rtc_configuration={
        "iceServers": token.ice_servers
    }
)
