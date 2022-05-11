import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from flask_login.utils import login_required
import plotly.express as px
import pandas as pd
from dash_application import navigation
import dash_bootstrap_components as dbc


#from urllib import response
#from urllib.request import urlopen
#import json

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

df3 = pd.DataFrame(
    {
        "types": ["Access Failure", "Communications Failure", "Data Issue", "Default", "Hardware Failure", "Performance Issue",
                  "Printing Failure", "Process Failure", "Security Issue", "Security Cyberattacks", "Software Failure", 
                  "Software Warning", "Telephone Failure"],
        "number": [3987, 153, 228, 161, 102, 851, 56, 181, 30, 23, 1919, 43, 53],
    }
)



df4 = pd.DataFrame(
    {
        "month": ["January", "February", "March", "April",
                  "January", "February", "March", "April",
                  "January", "February", "March", "April"],
        "number": [659, 727, 757, 837,
                   47,35,48, 37,
                   11,14,14,17
            ],
        "company": ["IBERIA", "IBERIA", "IBERIA", "IBERIA", 
                    "IAG CARGO", "IAG CARGO", "IAG CARGO", "IAG CARGO",  
                    "IBERIA EXPRESS", "IBERIA EXPRESS", "IBERIA EXPRESS", "IBERIA EXPRESS"]
    }
)






def create_dash_application(flask_app):
    dash_app = dash.Dash(server=flask_app, name="KPI1", url_base_pathname="/kpi1/", external_stylesheets=[dbc.themes.DARKLY])  
    dash_app.layout = html.Div(
        children=[
            navigation.navbar,
            html.H1(children="IBERIA INCIDENT REPORTS"),
            html.Div(
                children="""
            Incidences Numbers 
        """
            ),
            dcc.Graph(
                id="graph-2a",
                figure=px.pie(df2, values="number", names="types", title ="Incidences by type April"),
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
    dash_app = dash.Dash(server=flask_app, name="KPI2", url_base_pathname="/kpi2/", external_stylesheets=[dbc.themes.DARKLY])
    dash_app.layout = html.Div(
        children=[
            navigation.navbar,
            html.H1(children="IBERIA INCIDENT REPORTS"),
            html.Div(
                children="""
            Incidences Type last 2 months 
        """
            ),
            dcc.Graph(
                id="graph-2b",
                figure=px.pie(df3, values="number", names="types", title ="Incidences by type March"),
            )
        ]
    )

    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function]
            )

    return dash_app

def create_dash_application3(flask_app):
    dash_app = dash.Dash(server=flask_app, name="KPI3", url_base_pathname="/kpi3/", external_stylesheets=[dbc.themes.DARKLY])
    dash_app.layout = html.Div(
        children=[
            navigation.navbar,
            html.H1(children="IBERIA INCIDENT REPORTS"),
            html.Div(
                children="""
            Backlog incidents per company and month 
        """
            ),
            dcc.Graph(
                id="graph-3",
                figure=px.bar(df4, x="month", y="number", color = "company", title ="Backlog Incidences by company name"),
            ),
        ]
    )

    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function]
            )

    return dash_app











