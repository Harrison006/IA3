import requests
api_server = 'https://api.infrasolutions.au/api'

username = input("Username: ")

# url for Api Calls
base_url = api_server+'?username={}'
# format url
url = base_url.format(username)
        
response = requests.get(url)
json_respnose = response.json()

print(json_respnose) 