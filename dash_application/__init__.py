import dash
import dash_core_components as dcc
import dash_html_components as html
from flask_login.utils import login_required
import plotly.express as px
import pandas as pd

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame(
    {
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
    }
)


def create_dash_application(flask_app):
    dash_app = dash.Dash(server=flask_app, name="KPI1", url_base_pathname="/kpi1/")
    dash_app.layout = html.Div(
        children=[
            html.H1(children="IBERIA INCIDENT REPORTS"),
            html.Div(
                children="""
            KPI's Dashboard 
        """
            ),
            dcc.Graph(
                id="example-graph",
                figure=px.bar(df, x="Fruit", y="Amount", color="City", barmode="group"),
            ),
        ]
    )

    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function]
            )

    return dash_app

def create_dash_application2(flask_app):
    dash_app = dash.Dash(server=flask_app, name="KPI2", url_base_pathname="/kpi2/")
    dash_app.layout = html.Div(
        children=[
            html.H1(children="IBERIA INCIDENT REPORTS"),
            html.Div(
                children="""
            KPI's Dashboard 
        """
            ),
            dcc.Graph(
                id="example-graph",
                figure=px.bar(df, x="Fruit", y="Amount", color="City", barmode="group"),
            ),
        ]
    )

    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function]
            )

    return dash_app

def create_dash_application3(flask_app):
    dash_app = dash.Dash(server=flask_app, name="KPI3", url_base_pathname="/kpi3/")
    dash_app.layout = html.Div(
        children=[
            html.H1(children="IBERIA INCIDENT REPORTS"),
            html.Div(
                children="""
            KPI's Dashboard 
        """
            ),
            dcc.Graph(
                id="example-graph",
                figure=px.bar(df, x="Fruit", y="Amount", color="City", barmode="group"),
            ),
        ]
    )

    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function]
            )

    return dash_app











