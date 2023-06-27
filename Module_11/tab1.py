import dash
from dash import Dash, html, dcc, callback, Output, Input
import plotly.graph_objects as go

def render_tab(df):
    """
    we create a render_tab function that takes a database as an argument,
    we specify the default date range for the DatePickerRange widget.
    the layout consists of three basic elements: 
    header, fiels widget for selecting a time range, 
    and two charts located next to each other
    """
    layout = html.Div([html.H1('Total sales',style={'text-align':'center'}),
                        html.Div([dcc.DatePickerRange(id='sales-range',
                        start_date=df['tran_date'].min(),
                        end_date=df['tran_date'].max(),
                        display_format='YYYY-MM-DD')],style={'width':'100%','text-align':'center'}),
                        html.Div([html.Div([dcc.Graph(id='bar-sales')],style={'width':'50%'}),
                        html.Div([dcc.Graph(id='choropleth-sales')],style={'width':'50%'})],style={'display':'flex'})
                        ])

    return layout