import requests
from api import Datastore

first_name = 'test'
last_name = 'bloke'
email = 'test@gmail.com'
gender = 'male'
address = '123 m st'
suburb = 'place'
phone = '123456789'

db = Datastore()
api_test = db.add_patient(first_name, last_name, email, gender, address, suburb, phone)

print(api_test)