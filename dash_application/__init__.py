import dash
import dash_core_components as dcc
import dash_html_components as html
from flask_login.utils import login_required
import plotly.express as px
import pandas as pd

from urllib import response
from urllib.request import urlopen
import json

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

df2 = pd.DataFrame(
    {
        "types": ["Access Failure", "Communications Failure", "Data Issue", "Default", "Hardware Failure", "Performance Issue",
                  "Printing Failure", "Process Failure", "Security Issue", "Security Cyberattacks", "Software Failure", 
                  "Software Warning", "Telephone Failure"],
        "number": [4206, 128, 231, 216, 128, 752, 49, 216, 20, 16, 1728, 25, 75],
    }
)


response = urlopen("https://g986b1d252d1c63-db2022.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi1/incvol/")
df1 = json.loads(response.read())['items']


def create_dash_application(flask_app):
    dash_app = dash.Dash(server=flask_app, name="KPI1", url_base_pathname="/kpi1/")
    dash_app.layout = html.Div(
        children=[
            html.H1(children="IBERIA INCIDENT REPORTS"),
            html.Div(
                children="""
            Incidences Numbers 
        """
            ),
            dcc.Graph(
                id="graph-1a",
                figure=px.bar(df1, x="month", y="incidences_number", barmode="group"),
            ),
            dcc.Graph(
                id="graph-1b",
                figure=px.bar(df1, x="priority", y="incidences_number", barmode="group"),
            )
            
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
            Incidences Type 
        """
            ),
            dcc.Graph(
                id="graph-2a",
                figure=px.pie(df2, values="number", names="types", title ="Incidences by type"),
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
                figure=px.pie(df2, values="number", names="types", title ="Incidences by type"),
            ),
        ]
    )

    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function]
            )

    return dash_app











