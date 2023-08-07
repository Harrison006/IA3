from dash import Dash, html, dcc
import dash
import dash_table

app = Dash(__name__, use_pages=True)
app._favicon = ("images/rtrpng.png")
app.layout = html.Div([
    html.Link(rel='stylesheet', href='assets/header.css'),  # Link to the external CSS file
    # Rest of your layout code
    html.Div(
        className="app-header",
        children=[
            html.Div('Road to Recovery Home page', className="app-header--title")
        ]
    ),

    html.Div(
        className="button-container",  # Add a class to the container
        children=[
            html.Div(
                dcc.Link(
                    f"{page['name']}", href=page["relative_path"], className="custom-button"
                )
            )
            for page in dash.page_registry.values()
        ]
    ),

    dash.page_container
])
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port="9091")