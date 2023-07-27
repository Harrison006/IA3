import pandas as pd
import requests

response = requests.get('https://api.infrasolutions.au/api/get_clinician_stats?username=bahlin1')
with open("response.json", "w") as f:
    f.write(response.text)
#json_response = response.json()

# Incorporate data
df = pd.read_json('response.json')

print(df.to_string()) 