# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import json
import requests
import http.server

response = requests.get(
    "https://api.infrasolutions.au/api/get_clinician_stats?username=bahlin1"
)
with open("response.json", "w") as f:
    f.write(response.text)
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


#app.layout = html.Div(
#    [
#        html.Div(children="My First App with Data"),
#        dash_table.DataTable(data=df.to_string("records"), page_size=14, columns=[{"name": i, "id": i} for i in df.columns]),
#    ]
#)
"""
app.layout = html.Div([
dash_table.DataTable(
    data=df.to_string('records'),
    columns=[{"id": i, "name": i} for i in df.columns]
)
])
"""
# Add controls to build the interaction

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8060")
