# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

app = Dash(__name__)

colors = {"background": "#111111", "text": "#7FDBFF"}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame(
    {
        "Country": [
            "Australia",
            "New Zealand",
            "Sudan",
            "Iran",
            "Australia",
            "New Zealand",
            "Sudan",
            "Iran",
        ],
        "Population (millions)": [74.722, 25.97, 52, 48.75, 25.69, 5.084, 43.85, 83.99],
        "Species": [
            "Sheep",
            "Sheep",
            "Sheep",
            "Sheep",
            "Humans",
            "Humans",
            "Humans",
            "Humans",
        ],
    }
)

fig = px.bar(
    df, x="Country", y="Population (millions)", color="Species", barmode="group"
)

fig.update_layout(
    plot_bgcolor=colors["background"],
    paper_bgcolor=colors["background"],
    font_color=colors["text"],
)

app.layout = html.Div(
    style={"backgroundColor": colors["background"]},
    children=[
        html.H1(
            children="Hello KeyLead",
            style={"textAlign": "center", "color": colors["text"]},
        ),
        html.Div(
            children="Dash tutorial: A Knowledge Share presentation.",
            style={"textAlign": "center", "color": colors["text"]},
        ),
        dcc.Graph(id="example-graph-2", figure=fig),
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)

