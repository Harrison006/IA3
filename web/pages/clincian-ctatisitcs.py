# Import packages
from dash import Dash, html, dcc, callback, Output, Input, State
import dash
import pandas as pd
import dash_table
import requests
import io
from flask import Response

# Initialize the Dash app
dash.register_page(__name__, path='/clincian-ctatisitcs')

layout = html.Div(
    children=[
        html.H1("Clinician Stats Caller"),
        dcc.Input(id='text-input', type='text', placeholder='Enter Username...'),
        html.Button('Get Data', id='get-data-1', n_clicks=0),
        html.Div(id='output-1')
    ]
)

# Define callback to fetch data from API and display in a table
@callback(
    Output('output-1', 'children'),
    [Input('get-data-1', 'n_clicks')],
    [State('text-input', 'value')],
    prevent_initial_call=True
)
def fetch_data_from_api(n_clicks, input_value):

    if n_clicks > 0 and input_value:
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
                    output.append(table)
                else:
                    output.append(html.Div("No data available."))
            else:
                output.append(html.Div("API request failed."))
        except Exception as e:
            output.append(html.Div(f"Error: {str(e)}"))
    else:
        output.append(html.Div("Please enter something."))


