import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#Definir el exchange a usar
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

#Cola exclusiva para este consumidor
results = channel.queue_declare(queue='', exclusive=True)
queue_name = results.method.queue

severities = sys.argv[1:]
if not severities:
	sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
	sys.exit(1)

for severity in severities:
	channel.queue_bind(
		exchange='direct_logs', queue=queue_name, routing_key=severity)
#La cola se asigna a un 'exchange'

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
	print(" [x] %r:%r" % (method.routing_key, body))

channel.basic_consume(
	queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()