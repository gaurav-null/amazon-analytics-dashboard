import dash
from dash import dcc, html, Input, Output, State, callback_context
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import dash_bootstrap_components as dbc
import uuid
import random
from faker import Faker

fake = Faker()

DARK_THEME = {
    'background': '#1E1E2F',
    'card_background': '#2A2A3F',
    'text': '#FFFFFF',
    'primary': '#6A57FD',
    'secondary': '#FF7E5F',
    'accent1': '#00C9FF',
    'accent2': '#92FE9D',
    'success': '#00F260',
    'warning': '#FF7E5F',
    'gradient1': 'linear-gradient(135deg, #6A57FD, #00C9FF)',
    'gradient2': 'linear-gradient(135deg, #FF7E5F, #F9D423)',
}

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}]
)

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>Modern Analytics Dashboard</title>
        {%favicon%}
        {%css%}
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap" rel="stylesheet">
        <style>
            body {
                background-color: ''' + DARK_THEME['background'] + ''';
                font-family: 'Inter', sans-serif;
                color: ''' + DARK_THEME['text'] + ''';
            }
            .card {
                background: ''' + DARK_THEME['card_background'] + ''';
                border: none;
                border-radius: 15px;
                box-shadow: 8px 8px 15px rgba(0, 0, 0, 0.3),
                            -8px -8px 15px rgba(255, 255, 255, 0.05);
                margin-bottom: 1.5rem;
            }
            .card-header {
                background: ''' + DARK_THEME['gradient1'] + ''';
                color: white;
                font-weight: 500;
                border-radius: 15px 15px 0 0;
                padding: 1rem;
            }
            .dashboard-title {
                color: white;
                font-weight: bold;
                margin-bottom: 2rem;
                text-align: center;
                background: ''' + DARK_THEME['gradient2'] + ''';
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            .kpi-card {
                text-align: center;
                padding: 1.5rem;
                background: ''' + DARK_THEME['gradient1'] + ''';
                border-radius: 15px;
                color: white;
            }
            .kpi-value {
                font-size: 2.5rem;
                font-weight: bold;
            }
            .filter-label {
                font-weight: 500;
                margin-bottom: 0.5rem;
                color: ''' + DARK_THEME['text'] + ''';
            }
            .dash-graph {
                background: ''' + DARK_THEME['card_background'] + ''';
                border-radius: 15px;
                padding: 1rem;
            }
            .navbar {
                background: ''' + DARK_THEME['gradient1'] + ''';
                border-radius: 0 0 15px 15px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
            }
            .nav-link {
                color: white !important;
                font-weight: 500;
            }
            .nav-link.active {
                background: rgba(255, 255, 255, 0.1) !important;
                border-radius: 10px;
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

def create_header():
    return dbc.Navbar(
        dbc.Container([
            html.A(
                dbc.Row([
                    dbc.Col(html.Img(src="/logo.png", height="30px")),
                    dbc.Col(dbc.NavbarBrand("Modern Analytics Dashboard", className="ms-2")),
                ],
                align="center",
                ),
                href="/",
                style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(id="navbar-toggler"),
            dbc.Collapse(
                dbc.Nav([
                    dbc.NavItem(dbc.NavLink("Overview", href="#", active=True)),
                    dbc.NavItem(dbc.NavLink("Reports", href="#")),
                    dbc.NavItem(dbc.NavLink("Settings", href="#")),
                ]),
                id="navbar-collapse",
                navbar=True,
            ),
        ]),
        color="primary",
        dark=True,
        className="mb-4",
    )

def create_filters():
    return dbc.Card([
        dbc.CardHeader("Filters & Controls"),
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    html.Label("Date Range", className="filter-label"),
                    dcc.DatePickerRange(
                        id='date-filter',
                        start_date=events_df['timestamp'].min(),
                        end_date=events_df['timestamp'].max(),
                        className="mb-3"
                    )
                ], md=3),
                dbc.Col([
                    html.Label("Category", className="filter-label"),
                    dcc.Dropdown(
                        id='category-filter',
                        options=[{'label': cat, 'value': cat} 
                               for cat in products_df['category'].unique()],
                        multi=True,
                        placeholder="Select categories..."
                    )
                ], md=3),
                dbc.Col([
                    html.Label("Device", className="filter-label"),
                    dcc.Dropdown(
                        id='device-filter',
                        options=[{'label': dev.title(), 'value': dev} 
                               for dev in events_df['device'].unique()],
                        multi=True,
                        placeholder="Select devices..."
                    )
                ], md=3),
                dbc.Col([
                    html.Label("Price Range ($)", className="filter-label"),
                    dcc.RangeSlider(
                        id='price-range',
                        min=0,
                        max=1000,
                        step=50,
                        marks={i: f'${i}' for i in range(0, 1001, 200)},
                        value=[0, 1000]
                    )
                ], md=3),
            ]),
        ])
    ], className="mb-4")

app.layout = dbc.Container([
    create_header(),
    html.H1("Modern Analytics Dashboard", className="dashboard-title"),
    create_filters(),
    create_kpi_cards(),
    create_charts_section(),
], fluid=True)

if __name__ == '__main__':
    app.run_server(debug=True)