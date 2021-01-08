import pika
import sys

message = ' '.join(sys.argv[1:]) or "Hello World!"

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='colaBasica')

channel.basic_publish(exchange='',
					  routing_key='colaBasica',
					  body=message)

print(" [x] Sent %r" % message)

connection.close()