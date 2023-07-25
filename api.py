import requests

# api_server = 'https://api.infrasolutions.au/api'


class Datastore:
    def get_usernames(self):
        response = requests.get("https://api.infrasolutions.au/api/get_usernames")
        json_respnose = response.json()
        return json_respnose

    def get_staff_names(self):
        response = requests.get("https://api.infrasolutions.au/api/get_staff_names")
        json_respnose = response.json()
        return json_respnose

    def get_assessments(self, firstname, lastname):
        response = requests.get(
            "https://api.infrasolutions.au/api/get_assessments?firstname={}&lastname={}"
        )
        json_respnose = response.json()
        return json_respnose

    def add_patient(self, first_name, last_name, email, gender, address, suburb, phone):
        base_url = "https://api.infrasolutions.au/api/get_assessments?firstname={}&lastname={}&email={}&gender={}&address{}&suburb{}&phone={}"
        url = base_url.format(
            first_name, last_name, email, gender, address, suburb, phone
        )
        response = requests.put(url)
        json_response = response.json()
        return json_response

    def get_password(self, username):
        # url for Api Calls
        base_url = "https://api.infrasolutions.au/api/get_password?username={}"
        # format url
        url = base_url.format(username)
        # printing json response
        response = requests.get(url)
        json_respnose = response.json()
        return json_respnose

    def login(self, username, passowrd):
        
        # url for Api Calls
        base_url = "https://api.infrasolutions.au/api/get_password?username={}"
        # format url
        url = base_url.format(username)

        response = request.get(url)
        json_respnose = response.json()
        return json_respnose
        if passowrd == response:
            print("Success, you logged in!")
        else:
            print("Wrong password!")
        json_respnose = response.json()
