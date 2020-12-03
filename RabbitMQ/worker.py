import pika, sys, os
import time

def main():
	connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
	channel = connection.channel()


	#Checkear si hay cola con tal nombre
	channel.queue_declare(queue="colaBasica")
	channel.basic_qos(prefetch_count=1)

	#recibir mensajes (sobreescribir una funcion de devolucion de llamada "callback")
	def callback(ch, method, properties, body):
		print(" [x] Recived %r" % body.decode())
		time.sleep(10)
		print(" [x] Done")
		ch.basic_ack(delivery_tag = method.delivery_tag)

	channel.basic_consume(queue='colaBasica', on_message_callback=callback)

	print(' [*] Waiting for messages. To exit press CTRL+C')
	channel.start_consuming()

	#Bucle infinito
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print('Interrupted')
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)