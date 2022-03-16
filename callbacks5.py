# -*- coding: utf-8 -*-
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        dcc.Input(id="input-1-state", type="text", value="NOUN"),
        dcc.Input(id="input-2-state", type="text", value="PLURAL NOUN"),
        dcc.Input(id="input-3-state", type="text", value="VERB (PRESENT TENSE)"),
        dcc.Input(id="input-4-state", type="text", value="VERB (PRESENT TENSE)"),
        dcc.Input(id="input-5-state", type="text", value="PART OF BODY (PLURAL)"),
        dcc.Input(id="input-6-state", type="text", value="ADJECTIVE"),
        dcc.Input(id="input-7-state", type="text", value="PLURAL NOUN"),
        dcc.Input(id="input-8-state", type="text", value="ADJECTIVE"),
        html.Button(id="submit-button-state", n_clicks=0, children="Submit"),
        html.Div(id="output-state"),
    ]
)


@app.callback(
    Output("output-state", "children"),
    Input("submit-button-state", "n_clicks"),
    State("input-1-state", "value"),
    State("input-2-state", "value"),
    State("input-3-state", "value"),
    State("input-4-state", "value"),
    State("input-5-state", "value"),
    State("input-6-state", "value"),
    State("input-7-state", "value"),
    State("input-8-state", "value"),
)
def update_output(
    n_clicks, input1, input2, input3, input4, input5, input6, input7, input8
):
    if n_clicks == 0:
        return f"The Button has been pressed {n_clicks} times"
    else:
        str_6 = f"an {input6}" if input6[0] in "aeiouAEIOU" else f"a {input6}"
        return f"""
            The Button has been pressed {n_clicks} times.
            \n ***
            \n
            Today, every student has a computer small enough to fit into his {input1}. \n
            He can solve any math problem by simply pushing the computer's little {input2}. \n
            Computers can add, multiple, divide, and {input3}. \n
            They can also {input4} better than humans. \n
            Some computers are {input5}. \n
            Others have {str_6} screen that shows all kinds of {input7} and {input8} figures.
        """


if __name__ == "__main__":
    app.run_server(debug=True)
