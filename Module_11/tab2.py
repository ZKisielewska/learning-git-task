import dash
from dash import Dash, html, dcc, callback, Output, Input
import plotly.graph_objects as go

def render_tab(df):
    """
    we create a render_tab function that takes a database as an argument,
    layout consists of a header and an element stores two charts and a list of product categories,
    next we introduce the previously created pie chart to the layout,
    we add CSS elements to the tag that stores both charts and dropdown,
    dropdown contains three parameters: id, starting value, list of values to choose,
    in the end we create bar chart
    """
    grouped = df[df['total_amt']>0].groupby('prod_cat')['total_amt'].sum()
    fig = go.Figure(data=[go.Pie(labels=grouped.index,values=grouped.values)],layout=go.Layout(title='Share of product groups in sales'))

    layout = html.Div([html.H1('Products',style={'text-align':'center'}),

                        html.Div([html.Div([dcc.Graph(id='pie-prod-cat',figure=fig)],style={'width':'50%'}),
                        html.Div([dcc.Dropdown(id='prod_dropdown',
                                    options=[{'label':prod_cat,'value':prod_cat} for prod_cat in df['prod_cat'].unique()],
                                    value=df['prod_cat'].unique()[0]),
                                    dcc.Graph(id='barh-prod-subcat')],style={'width':'50%'})],style={'display':'flex'}),
                                    html.Div(id='temp-out')
                        ])

    return layout