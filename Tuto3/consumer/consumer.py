import pika
import time
import os

time.sleep(20)

HOST=os.environ['RABBITMQ_HOST']

connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST))
channel = connection.channel()

#El consumidor utiliza el exchange 'nestor'
channel.exchange_declare(exchange='nestor', exchange_type='fanout')

#Se crea una cola temporaria exclusiva para este consumidor
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

#La cola se asigna a un exchange
channel.queue_bind(exchange='nestor', queue=queue_name)

print(' [x] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
	print(" [x]  %r" % body)

channel.basic_consume(
	queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()