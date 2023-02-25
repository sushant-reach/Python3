
from twilio.rest import Client

VIRTUAL_TWILIO_NUMBER = "+12406502544"
VERIFIED_NUMBER = "+919421036342"
TWILIO_SID = "AC1283ad1c2a524b23c72ac816b6888844"
TWILIO_AUTH_TOKEN = "085831dbdf3e5ffce9b63c22ca7c499f"

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    #TODO 8. - Send each article as a separate message via Twilio.
article = "This is Test Message"

message = client.messages.create(
    body=article,
    from_=VIRTUAL_TWILIO_NUMBER,
    to=VERIFIED_NUMBER
)