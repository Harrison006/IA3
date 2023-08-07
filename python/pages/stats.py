# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input, register_page
import pandas as pd
import plotly.express as px
import json
import requests
import http.server
import csv

username = "<username>"

response = requests.get(
    "https://api.infrasolutions.au/api/get_clinician_stats?username=bahlin1"
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
# Incorporate data
df = pd.read_csv("./response.csv")
print(df)
# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div(children='Clinician Stats'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=50)
])

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8040")
    register_page(__name__, path="/<username>")