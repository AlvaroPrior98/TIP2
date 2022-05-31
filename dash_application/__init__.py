import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from flask_login.utils import login_required
import plotly.express as px
import pandas as pd
from dash_application import navigation
import dash_bootstrap_components as dbc
import csv
from collections import Counter


#from urllib import response
#from urllib.request import urlopen
#import json

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options


#Reading April's csv file for Icnident Type

incidences_april = []


with open('april.csv', 'r', encoding = 'utf8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')  
    
    for skip in range(4):
        next(csv_reader)

    
    for line in csv_reader:
        incidences_april.append(line[14])
        
data_april = dict(Counter(incidences_april))
inc_types_april = data_april.keys()
inc_number_april = data_april.values()

final_data_april = {"types": inc_types_april, "number": inc_number_april}

df2 = pd.DataFrame(final_data_april)



#Reading March's csv file for Incident Type

incidences_march = []


with open('march.csv', 'r', encoding = 'utf8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')  
    
    for skip in range(4):
        next(csv_reader)

    
    for line in csv_reader:
        incidences_march.append(line[14])
        
data_march = dict(Counter(incidences_march))
inc_types_march = data_march.keys()
inc_number_march = data_march.values()

final_data_march = {"types": inc_types_march, "number": inc_number_march}

df3 = pd.DataFrame(final_data_march)



#Reading April's csv file for Incident Status

status_april = []


with open('april.csv', 'r', encoding = 'utf8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')  
    
    for skip in range(4):
        next(csv_reader)

    
    for line in csv_reader:
        status_april.append(line[3])
        
data_status_april = dict(Counter(status_april))
inc_status_april = data_status_april.keys()
inc_status_number_april = data_status_april.values()

final_data_status_april = {"status": inc_status_april, "number": inc_status_number_april}

df4 = pd.DataFrame(final_data_status_april)






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
                figure=px.bar(df4, x="status", y="number", title ="Backlog Incidences by company name"),
            ),
        ]
    )

    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function]
            )

    return dash_app











