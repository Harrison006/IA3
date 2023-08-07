# Import packages
from dash import Dash, html, dcc, callback, Output, Input, State
import dash
import pandas as pd
import dash_table
import requests
import io
from flask import Response, Flask, request

# Initialize the Dash app
dash.register_page(__name__, path='/add-assesment')

layout = html.Div(
    children=[
        html.H1("Exercise Regimes"),
        
        html.Div([
            html.Label('Patient ID'),
            dcc.Input(id='text-input-3', type='text', placeholder='Enter Patient ID...')
        ], className='input-container'),

        html.Div([
            html.Label('Clinician Username'),
            dcc.Input(id='clinician-input', type='text', placeholder='Clinician username...')
        ], className='input-container'),

        html.Div([
            html.Label('Date'),
            dcc.Input(id='date-input', placeholder='Select Date...')
        ], className='input-container'),

        html.Div([
            html.Label('Hip Flexors'),
            dcc.Input(id='hip-flexors-input', type='text', placeholder='Hip Flexors...')
        ], className='input-container'),

        html.Div([
            html.Label('Knee Extensors'),
            dcc.Input(id='knee-extensors-input', type='text', placeholder='Knee Extensors...')
        ], className='input-container'),

        html.Div([
            html.Label('Dorsiflexors'),
            dcc.Input(id='dorsiflexors-input', type='text', placeholder='Dorsiflexors...')
        ], className='input-container'),

        html.Div([
            html.Label('Great Toe Extensor'),
            dcc.Input(id='great-toe-extensor-input', type='text', placeholder='Great Toe Extensor...')
        ], className='input-container'),

        html.Div([
            html.Label('Plantar Flexors'),
            dcc.Input(id='plantar-flexors-input', type='text', placeholder='Plantar Flexors...')
        ], className='input-container'),

        html.Div([
            html.Label('Shoulder Abductors'),
            dcc.Input(id='shoulder-abductors-input', type='text', placeholder='Shoulder Abductors...')
        ], className='input-container'),

        html.Div([
            html.Label('Elbow Flexors'),
            dcc.Input(id='elbow-flexors-input', type='text', placeholder='Elbow Flexors...')
        ], className='input-container'),

        html.Div([
            html.Label('Elbow Extensors'),
            dcc.Input(id='elbow-extensors-input', type='text', placeholder='Elbow Extensors...')
        ], className='input-container'),

        html.Div([
            html.Label('Wrist Extensors'),
            dcc.Input(id='wrist-extensors-input', type='text', placeholder='Wrist Extensors...')
        ], className='input-container'),

        html.Div([
            html.Label('Finger Flexors'),
            dcc.Input(id='finger-flexors-input', type='text', placeholder='Finger Flexors...')
        ], className='input-container'),

        html.Div([
            html.Label('Hand Intrinsics'),
            dcc.Input(id='hand-intrinsics-input', type='text', placeholder='Hand Intrinsics...')
        ], className='input-container'),

        html.Div([
            html.Label('Aphasia'),
            dcc.Input(id='aphasia-input', type='text', placeholder='Aphasia...')
        ], className='input-container'),

        html.Div([
            html.Label('Apraxia'),
            dcc.Input(id='apraxia-input', type='text', placeholder='Apraxia...')
        ], className='input-container'),

        html.Div([
            html.Label('Dysarthria'),
            dcc.Input(id='dysarthria-input', type='text', placeholder='Dysarthria...')
        ], className='input-container'),

        html.Div([
            html.Label('Dysphonia'),
            dcc.Input(id='dysphonia-input', type='text', placeholder='Dysphonia...')
        ], className='input-container'),

        html.Div([
            html.Label('Memory'),
            dcc.Input(id='memory-input', type='text', placeholder='Memory...')
        ], className='input-container'),

        html.Div([
            html.Label('Attention'),
            dcc.Input(id='attention-input', type='text', placeholder='Attention...')
        ], className='input-container'),

        html.Div([
            html.Label('Judgement'),
            dcc.Input(id='judgement-input', type='text', placeholder='Judgement...')
        ], className='input-container'),

        html.Div([
            html.Label('Neglect'),
            dcc.Input(id='neglect-input', type='text', placeholder='Neglect...')
        ], className='input-container'),

        html.Div([
            html.Button('Post Data', id='post-data', n_clicks=0)
        ], className='input-container'),

        html.Div(id='output-3')
    ]
)

# Define callback to fetch data from API and display in a table
@callback(
    Output('output-3', 'children'),
    [Input('post-data', 'n_clicks')],
    [State('text-input-3', 'value'),
     State('clinician-input', 'value'),
     State('date-input', 'value'),
     State('hip-flexors-input', 'value'),
     State('knee-extensors-input', 'value'),
     State('dorsiflexors-input', 'value'),
     State('great-toe-extensor-input', 'value'),
     State('plantar-flexors-input', 'value'),
     State('shoulder-abductors-input', 'value'),
     State('elbow-flexors-input', 'value'),
     State('elbow-extensors-input', 'value'),
     State('wrist-extensors-input', 'value'),
     State('finger-flexors-input', 'value'),
     State('hand-intrinsics-input', 'value'),
     State('aphasia-input', 'value'),
     State('apraxia-input', 'value'),
     State('dysarthria-input', 'value'),
     State('dysphonia-input', 'value'),
     State('memory-input', 'value'),
     State('attention-input', 'value'),
     State('judgement-input', 'value'),
     State('neglect-input', 'value')],
    prevent_initial_call=True
)
def post_data_to_api(n_clicks, username, clinician, date, hip_flexors, knee_extensors, dorsiflexors, great_toe_extensor,
                     plantar_flexors, shoulder_abductors, elbow_flexors, elbow_extensors, wrist_extensors,
                     finger_flexors, hand_intrinsics, aphasia, apraxia, dysarthria, dysphonia, memory,
                     attention, judgement, neglect):
    if n_clicks > 0 and username:
        try:

            api_url = f'https://api.infrasolutions.au/api/add_assessments?clinician={clinician}&patient_id={username}&date={date}&hip_flexors={hip_flexors}&knee_extensors={knee_extensors}&dorsiflexors={dorsiflexors}&great_toe_extensor={great_toe_extensor}&plantar_flexors={plantar_flexors}&shoulder_abductors={shoulder_abductors}&elbow_flexors={elbow_flexors}&elbow_extensors={elbow_extensors}&wrist_extensors={wrist_extensors}&finger_flexors={finger_flexors}&hand_intrinsics={hand_intrinsics}&aphasia={aphasia}&apraxia={apraxia}&dysarthria={dysarthria}&dysphonia={dysphonia}&memory={memory}&attention={attention}&judgement={judgement}&neglect={neglect}'
            response = requests.get(api_url)

            if response.status_code == 200:
                return [html.Div("Data posted successfully.")]
            else:
                return [html.Div("API request failed.")]
        except Exception as e:
            return [html.Div(f"Error: {str(e)}")]
    else:
        return [html.Div("Please enter a username.")]
