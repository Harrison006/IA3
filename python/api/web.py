from dash import Dash, html, dcc
import dash

app = Dash(__name__, use_pages=True, pages_folder=".")

app.layout = html.Div([
	html.H1('Multi-page app with Dash Pages'),

    html.Div(
        [
            html.Div(
                dcc.Link(
                    f"{page['name']} - {page['path']}", href=page["relative_path"]
                )
            )
            for page in dash.page_registry.values()
        ]
    ),

	dash.page_container
])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="9091")