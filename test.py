import requests
from api import Datastore

db = Datastore()

print(db.get_assessments())