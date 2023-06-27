from dash import html, dcc
import plotly.graph_objects as go

def render_tab(df):

    layout = html.Div([html.H1('Store type by day of week',style={'text-align':'center'}),

                        
                        html.Div([dcc.Dropdown(id='store_dropdown',
                                    options=[{'label':Store_type,'value':Store_type} for Store_type in df['Store_type'].unique()],
                                    value=df['Store_type'].unique()[0]),
                                    dcc.Graph(id='pie-store-type')],style={'width':'50%'}),
                                    html.Div(id='temp-out'),
                        html.Div([dcc.Dropdown(id='day_dropdown',
                                    options=[{'label':day,'value':day} for day in df['tran_date_day_name'].unique()],
                                    value=df['tran_date_day_name'].unique()[0]),
                                    dcc.Graph(id='pie-day')],style={'width':'50%'}),
                                    html.Div(id='temp-out')
                        ])




    return layout