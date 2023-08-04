# Python program to convert
# JSON file to CSV
import json
import csv
import requests
# Opening JSON file and loading the data
# into the variable data


response = requests.get(
    "https://api.infrasolutions.au/api/get_clinician_stats?username=bahlin1"
)
with open("response.json") as json_file:
    data = json.load(json_file)
employee_data = data["results"]
# now we will open a file for writing
data_file = open("response.csv", "w")
# create the csv writer object
csv_writer = csv.writer(data_file)
# Counter variable used for writing
# headers to the CSV file
count = 0
for emp in employee_data:
    if count == 0:
        # Writing headers of CSV file
        header = emp.keys()
        csv_writer.writerow(header)
        count += 1
    # Writing data of CSV file
    csv_writer.writerow(emp.values())
data_file.close()
"""
import pandas as pd
import requests
import json

response = requests.get('https://api.infrasolutions.au/api/get_clinician_stats?username=bahlin1')
with open("response.json", "w") as f:
    f.write(response.text)
#json_response = response.json()

# Incorporate data
df = pd.read_json('response.json')
jsonres = './response.json'
print(df.to_string()) 
"""
