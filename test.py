import requests
from api import Datastore

db = Datastore()
api_test = db.get_password('delcy9')

print(api_test)