from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from math import factorial as fact

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        dcc.Input(id="num-multi", type="number", value=5),
        html.Table(
            [
                html.Tr([html.Td(["x", html.Sup(2)]), html.Td(id="square")]),
                html.Tr([html.Td(["x", html.Sup(3)]), html.Td(id="cube")]),
                html.Tr([html.Td([2, html.Sup("x")]), html.Td(id="twos")]),
                html.Tr([html.Td([3, html.Sup("x")]), html.Td(id="threes")]),
                html.Tr([html.Td(["x", html.Sup("x")]), html.Td(id="x^x")]),
                html.Tr([html.Td(["x!"]), html.Td(id="x!")]),
            ]
        ),
    ]
)


@app.callback(
    Output("square", "children"),
    Output("cube", "children"),
    Output("twos", "children"),
    Output("threes", "children"),
    Output("x^x", "children"),
    Output("x!", "children"),
    Input("num-multi", "value"),
)
def callback_a(x):
    return x ** 2, x ** 3, 2 ** x, 3 ** x, x ** x, fact(x)


if __name__ == "__main__":
    app.run_server(debug=True)

