# Import packages
from dash import Dash, html, dcc, callback, Output, Input, State
import dash
import pandas as pd
import dash_table
import requests
import io
from flask import Response

# Initialize the Dash app
Dash.register_page(__name__, path='/stats')

layout = html.Div(children=[
    html.H1("Clinician Stats Caller"),
    dcc.Input(id='text-input', type='text', placeholder='Enter Username...'),
    html.Button('Get Data', id='get-data-button', n_clicks=0),
    html.Div(id='output-container')
])

# Define callback to fetch data from API and display in a table
@app.callback(
    Output('output-container', 'children'),
    [Input('get-data-button', 'n_clicks')],
    [State('text-input', 'value')]
)
def fetch_data_from_api(n_clicks, input_value):
    if n_clicks > 0:
        if input_value:
            try:
                # Replace 'API_URL' with the actual API URL
                response = requests.get(f'https://api.infrasolutions.au/api/get_clinician_stats?username={input_value}')

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
            return html.Div("Please enter something.")

