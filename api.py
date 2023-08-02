import requests

# api_server = 'https://api.infrasolutions.au/api'


class Datastore:
    def get_usernames(self):
        # url for Api Calls
        response = requests.get("https://api.infrasolutions.au/api/get_usernames")
        json_respnose = response.json()
        return json_respnose

    def get_staff_names(self):
        # url for Api Calls
        response = requests.get("https://api.infrasolutions.au/api/get_staff_names")
        json_respnose = response.json()
        return json_respnose

    def get_assessments(self, firstname, lastname):
        # url for Api Calls
        response = requests.get(
            f"https://api.infrasolutions.au/api/get_assessments?firstname={firstname}&lastname={lastname}"
        )    # Using an F string to demonstrate different types of ways of inserting varibles into code
        
        json_respnose = response.json()
        return json_respnose

    def add_patient(self, first_name, last_name, email, gender, address, suburb, phone):
        # Initial URL for the API
        base_url = "https://api.infrasolutions.au/api/add_patient?first_name={}&last_name={}&email={}&gender={}&address={}&suburb={}&phone={}"
        url = base_url.format(
            first_name, last_name, email, gender, address, suburb, phone
        ) # Formating the URL afterwards with the correct varibles 
        response = requests.post(url)
        # Calling the API
        return response
        # Returning the response
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
