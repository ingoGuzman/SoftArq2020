import pymongo
import os

DATABASE="bot"
COLLECTION="frases"

def dbpopulate():
	myclient = pymongo.MongoClient(host=os.environ['MONGO_HOST'], port=int(os.environ['MONGO_PORT']))
	db = myclient[DATABASE]
	col = db[COLLECTION]

	misFrases= [
		{ "text": "Hola"},
		{ "text": "Chao"},
		{ "text": "AAAA"},
		{ "text": "BBBB"},
		{ "text": "asdjasd"},
		{ "text": "Carpe Diem"},
		{ "text": "Aloha"},
		{ "text": "Que todo fluya y nada influya"},
		{ "text": "Rocio te amo"},
		{ "text": "Holasdasdja"},
		{ "text": "Holaasdasd"},
		{ "text": "Hassd"},
		{ "text": "Holajasdhjasjh"},
		{ "text": "Holaadajdjsa"},
		{ "text": "Holaasjajd"},
		{ "text": "Empanada de pino"},
		{ "text": "Empanada de queso"},
	]

	col.insert_many(misFrases)

	return (True)