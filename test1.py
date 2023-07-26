import requests

first_name = 'test'
last_name = 'bloke'
#email = 'test@gmail.com'
#gender = 'male'
address = '123st'
suburb = 'place'
#phone = '123456789'


base_url = "https://api.infrasolutions.au/api/add_patient?firstname={}&lastname={}&email={}&gender={}&address{}&suburb{}&phone={}"
url = base_url.format(first_name, last_name, email, gender, address, suburb, phone)

response = requests.post(url)

print(response) 