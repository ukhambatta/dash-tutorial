# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc

app = Dash(__name__)

app.layout = html.Div(
    [
        html.Div(
            children=[
                html.Label("Dropdown"),
                dcc.Dropdown(["Key", "Lead", "Health"], "Health"),
                html.Br(),
                html.Label("Multi-Select Dropdown"),
                dcc.Dropdown(["Key", "Lead", "Health"], ["Key", "Health"], multi=True,),
                html.Br(),
                html.Label("Radio Items"),
                dcc.RadioItems(["Key", "Lead", "Health"], "Lead"),
            ],
            style={"padding": 10, "flex": 1},
        ),
        html.Div(
            children=[
                html.Label("Checkboxes"),
                dcc.Checklist(["Key", "Lead", "Health"], []),
                html.Br(),
                html.Label("Text Input"),
                dcc.Input(value="KeyLead Health", type="text"),
                html.Br(),
                html.Label("Slider"),
                dcc.Slider(
                    min=0,
                    max=9,
                    marks={i: f"Label {i}" if i == 1 else str(i) for i in range(1, 10)},
                    value=9,
                ),
            ],
            style={"padding": 10, "flex": 1},
        ),
    ],
    style={"display": "flex", "flex-direction": "row"},
)

if __name__ == "__main__":
    app.run_server(debug=True)

