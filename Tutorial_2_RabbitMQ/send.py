import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhos'))
channel = connection.channel()

channel.queue_declare(queue='colaBasica')

channel.basic_publish(exchange='',
					  routing_key='colaBasica',
					  body='Hello World!')

print(" [x] Sent 'Hello World!'")

connection.close()