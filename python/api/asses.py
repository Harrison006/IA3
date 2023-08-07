# Import packages
from dash import Dash, html, dcc, callback, Output, Input, State
import dash
import pandas as pd
import dash_table
import requests
import io
from flask import Response

# Initialize the Dash app


Dash.register_page(__name__, path='/asses')

layout = html.Div(children=[
    html.H1("Patient Stats"),
    dcc.Input(id='text-first', type='text', placeholder='Enter firstname...'),
    dcc.Input(id='text-last', type='text', placeholder='Enter lastname...'),
    html.Button('Get Data', id='get-data-button', n_clicks=0),
    html.Div(id='output-container')
])

# Define callback to fetch data from API and display in a table
@app.callback(
    Output('output-container', 'children'),
    [Input('get-data-button', 'n_clicks')],
    [State('text-first', 'value'),
     State('text-last', 'value')]
)
def fetch_data_from_api(n_clicks, first_name, last_name):
    if n_clicks > 0 and first_name and last_name:
        try:
            # Replace 'API_URL' with the actual API URL
            response = requests.get(f'https://api.infrasolutions.au/api/get_assessments?first_name={first_name}&last_name={last_name}')

            if response.status_code == 200:
                api_data = response.json()  # Parse JSON data from the response
                employee_data = api_data.get("results", [])

                if employee_data:
                    # Create a DataFrame from the JSON data
                    df = pd.DataFrame(employee_data)
                    
                    # Create a Dash DataTable component
                    table = dash_table.DataTable(
                        data=df.to_dict('records'),
                        columns=[{'name': col, 'id': col} for col in df.columns],
                        style_table={'height': '300px', 'overflowY': 'auto'}
                    )
                    return table
                else:
                    return html.Div("No data available.")
            else:
                return html.Div("API request failed.")
        except Exception as e:
            return html.Div(f"Error: {str(e)}")
    else:
        return html.Div("Please fill in both first name and last name.")

