# Import packages
import dash
import dash_table
import pandas as pd
import requests
from dash import html, callback, Output, Input, State

# Register the page
dash.register_page(__name__, path='/patient-all')

# Define the layout of the app
layout = html.Div(children=[
    html.H1("All patients"),
    html.Button('Get Data', id='get-data-1', n_clicks=0),
    html.Div(id='output-1')
])

# Define callback to fetch data from API and display in a table
@callback(
    Output('output-1', 'children', allow_duplicate=True),
    [Input('get-data-1', 'n_clicks')],
    prevent_initial_call=True
)
def fetch_and_display_data(n_clicks):
    output = []

    if n_clicks > 0:
        try:
            # Replace 'API_URL' with the actual API URL
            response = requests.get('https://api.infrasolutions.au/api/get_all_patient')

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
                        style_table={'height': 'auto', 'overflowY': 'auto'}
                    )
                    return table
                else:
                    return html.Div("No data available.")
            else:
                return html.Div("API request failed.")
        except Exception as e:
            return html.Div(f"Error: {str(e)}")
    else:
        return html.Div("Carked.")
    
    return Output