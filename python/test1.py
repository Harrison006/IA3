import requests

first_name = 'test'
last_name = 'bloke'
email = 'test'
gender = 'male'
address = '123st'
suburb = 'place'
phone = '123456789'


base_url = f"https://api.infrasolutions.au/api/add_patient?first_name={first_name}&last_name={last_name}&email={email}&gender={gender}&address={address}&suburb={suburb}&phone={phone}"
#url = base_url.format(, , , , , , )

response = requests.post(base_url)

print(base_url) 