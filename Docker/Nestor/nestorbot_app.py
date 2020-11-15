from slack import WebClient
from nestorbot import NestorBot
import populate
import os
import time

# Create a slack client
token=os.environ.get("SLACK_T1")+os.environ.get("SLACK_T2")
slack_web_client = WebClient(token)

# Get a new NestorBot
nestor_bot = NestorBot("#general")

if populate.dbpopulate():
	print("Nice")
else:
	print("Not nice")

# Get the onboarding message payload

# Post the onboarding message in Slack
for i in range (20):
	message = nestor_bot.get_message_payload()
	slack_web_client.chat_postMessage(**message)
	time.sleep(15)
