import dash
from dash import html, dcc
import dash_table

dash.register_page(__name__, path='/')

layout = html.Div(
    className="",
    children=[
    html.H1(
        children='Home page'),
    html.Img(src=r'assets/images/rtrpng.png', alt='image',width="auto", height="200"),
    html.Div(children='''
        Road to Recovery Home page for Clinicians.
    '''),
])