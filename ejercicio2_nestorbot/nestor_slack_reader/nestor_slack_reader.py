import pika
import sys
import time
import os

time.sleep(30)

HOST=os.environ['RABBITMQ_HOST']

connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST))
channel = connection.channel()

#El consumidor utiliza el exchange 'nestor'
channel.exchange_declare(exchange='nestor', exchange_type='topic', durable=True)

message1="[traducir] Hola mundo"
message2="[wikipedia] Michel Jackson"

channel.basic_publish(exchange="nestor", routing_key='traducir', body=message1)

channel.basic_publish(exchange="nestor", routing_key='wikipedia', body=message2)

print(' [x] Sent %r' % message1)
print(' [x] Sent %r' % message2)
connection.close()