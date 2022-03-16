# -*- coding: utf-8 -*-
from dash import Dash, dcc, html, Input, Output

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = Dash(__name__, external_stylesheets=external_stylesheets)

all_options = {
    "KeyLead Health": ["Andi Partovi", "Robert Tran", "Uriah Khambatta"],
    "Google": ["Sundar Pichai", "Jeremy Joslin", "Erica Son"],
    "Tesla": ["Elon Musk", "Ryan Scott", "Aryaman Pandav"],
}
app.layout = html.Div(
    [
        dcc.RadioItems(
            list(all_options.keys()), "KeyLead Health", id="companies-radio",
        ),
        html.Hr(),
        dcc.RadioItems(id="people-radio"),
        html.Hr(),
        html.Div(id="display-selected-values"),
    ]
)


@app.callback(Output("people-radio", "options"), Input("companies-radio", "value"))
def set_cities_options(selected_company):
    return [{"label": i, "value": i} for i in all_options[selected_company]]


@app.callback(Output("people-radio", "value"), Input("people-radio", "options"))
def set_cities_value(available_options):
    return available_options[0]["value"]


@app.callback(
    Output("display-selected-values", "children"),
    Input("companies-radio", "value"),
    Input("people-radio", "value"),
)
def set_display_children(selected_company, selected_person):
    ceos = ["Andi Partovi", "Sundar Pichai", "Elon Musk"]
    employees = ["Robert Tran", "Jeremy Joslin", "Ryan Scott"]
    str_descriptor = (
        "a CEO"
        if selected_person in ceos
        else "an employee"
        if selected_person in employees
        else "an intern"
    )

    return f"{selected_person} is {str_descriptor} at {selected_company}"


if __name__ == "__main__":
    app.run_server(debug=True)
