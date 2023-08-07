response = requests.get(
    f"https://api.infrasolutions.au/api/get_clinician_stats?username={username}"
)
if response.status_code == 200:
    api_data = response.json()  # Parse JSON data from the response
    output_filename = 'api_data.json'

    # Write JSON data to a file
    with open(output_filename, 'w') as output_file:
        json.dump(api_data, output_file, indent=4)

with open("api_data.json") as json_file:
    data = json.load(json_file)
employee_data = data["results"]
# now we will open a file for writing
data_file = open("js.csv", "w")
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