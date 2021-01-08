from persistence import connect_database, get_mongo_port, get_database_name, db_write
import pytest

@pytest.fixture
def database_name():
	return "nestor"
@pytest.fixture
def collection_name():
	return "test_persistance"

def test_connect_database():
	conection = connect_database()
	assert conection is not None

def test_check_port_type():
	port = get_mongo_port()
	assert type(port) is int

def test_database_name():
	db_name = get_database_name()
	assert db_name == "nestor"

def test_db_write(database_name, collection_name):
	db = connect_database()
	nb_doc_before = db[collection_name].count_documents({})

	db_write_message = "Hola"
	db_write(db_write_message, database_name, collection_name)

	nb_doc_after = db[collection_name].count_documents({})

	assert nb_doc_after-1 == nb_doc_before