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
with open("./response.json") as json_file:
    data = json.load(json_file)