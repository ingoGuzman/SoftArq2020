import pika, sys, os

def main():
	connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
	channel = connection.channel()


	#Checkear si hay cola con tal nombre
	channel.queue_declare(queue="colaBasica")

	#recibir mensajes (sobreescribir una funcion de devolucion de llamada "callback")
	def callback(ch, method, properties, body):
		print(" [x] Recived %r" % body)

	channel.basic_consume(queue='colaBasica', on_message_callback=callback, auto_ack=True)

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