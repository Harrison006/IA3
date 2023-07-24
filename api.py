import requests


class Datastore():
    def get_usernames(self):
        response = requests.get('https://api.infrasolutions.au/api/get_usernames')
        json_respnose = response.json()
        return json_respnose
    
    def get_staff_names(self):
        response = requests.get('https://api.infrasolutions.au/api/get_staff_names')
        json_respnose = response.json()
        return json_respnose
    
    def get_assessments(self, firstname, lastname):
        response = requests.get('https://api.infrasolutions.au/api/get_assessments?firstname={firstname}&lastname={lastname}')
        json_respnose = response.json()
        return json_respnose
    
    def add_patient(self, first_name, last_name, email, gender, address, suburb, phone):
        response = requests.get('https://api.infrasolutions.au/api/get_assessments?firstname={firstname}&lastname={lastname}&email={email}&gender={gender}&address{address}&suburb{suburb}&phone={phone}')
        json_response = response.json()
        return json_response
    
    def get_password(self, username):
        response = requests.get('https://api.infrasolutions.au/api/get_password?username={username}')
        json_respnose = response.json()
        return json_respnose