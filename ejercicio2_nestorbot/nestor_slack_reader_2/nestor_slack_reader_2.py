import pika
import sys
import time
import os
import logging
from flask import Flask
from slackeventsapi import SlackEventAdapter
from slack import WebClient


time.sleep(30)

##Rabbit mq

HOST=os.environ["RABBITMQ_HOST"]

connection=pika.BlockingConnection(pika.ConnectionParameters(host=HOST))
channel=connection.channel()

#exchange declaration
channel.exchange_declare(exchange="nestor", exchange_type="topic", durable=True)

##Flask
app = Flask(__name__)
##Event adapter too
SLACK_SECRET = os.environ.get("SLACK_S1")+os.environ.get("SLACK_S2")
SLACK_TOKEN = os.environ.get("SLACK_T1")+os.environ.get("SLACK_T2")

slack_events_adapter = SlackEventAdapter(SLACK_SECRET, "/slack/events", app)
print(SLACK_SECRET)

##WebClient
slack_web_client = WebClient(SLACK_TOKEN)
print(SLACK_TOKEN)

#flask app route example
@app.route("/")
def hello():
	return "Hello there!"

@slack_events_adapter.on("message")
def message(payload):
	"""Parse the message event
	"""
	# Get event data from payload
	event = payload.get("event", {})
	#Get the text
	text=event.get("text")

	if text.startswith("[traducir]"):
		channel.basic_publish(exchange="nestor", routing_key="traducir", body=text)

	if text.startswith("[wikipedia]"):
		channel.basic_publish(exchange="nestor", routing_key="wikipedia", body=text)

if __name__=="__main__":
	#create the logging object
	logger = logging.getLogger()
	logger.setLevel(logging.DEBUG)
	logger.addHandler(logging.StreamHandler())
	#Run our app on our externally facing ip address on port 3000 insteaf o running it on localhost wich is traditional for development
	app.run(host='0.0.0.0', port=3000)