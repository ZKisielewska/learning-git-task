import pandas as pd
import datetime as dt
import os
import dash
from dash import Dash, html, dcc, callback, Output, Input
import plotly.graph_objects as go
import tab1
import tab2
import tab3
import tab4

class db:
    def __init__(self):
        """class constructor load individual csv files into variables"""
        self.transactions = db.transation_init()
        self.cc = pd.read_csv(r'C:\Users\kisie\Downloads\db\db\country_codes.csv',index_col=0)
        self.customers = pd.read_csv(r'C:\Users\kisie\Downloads\db\db\customers.csv',index_col=0)
        self.prod_info = pd.read_csv(r'C:\Users\kisie\Downloads\db\db\prod_cat_info.csv')
        
    @staticmethod
    def transation_init():
        """cancatenate all files of transactions_db into one database with os library"""
        transactions = pd.DataFrame()
        src = r'C:\Users\kisie\Downloads\db\db\transactions'
        for filename in os.listdir(src):
            transactions = transactions.append(pd.read_csv(os.path.join(src,filename),index_col=0))

        def convert_dates(x):
            """convert date into the same type"""
            try:
                return dt.datetime.strptime(x,'%d-%m-%Y')
            except:
                return dt.datetime.strptime(x,'%d/%m/%Y')

        transactions['tran_date'] = transactions['tran_date'].apply(lambda x: convert_dates(x))

        return transactions
    
    def merge(self):
        """connect the transaction database with the appropriate product categories, customer and country of sale"""
        df = self.transactions.join(self.prod_info.drop_duplicates(subset=['prod_cat_code'])
        .set_index('prod_cat_code')['prod_cat'],on='prod_cat_code',how='left')

        df = df.join(self.prod_info.drop_duplicates(subset=['prod_sub_cat_code'])
        .set_index('prod_sub_cat_code')['prod_subcat'],on='prod_subcat_code',how='left')

        df = df.join(self.customers.join(self.cc,on='country_code')
        .set_index('customer_Id'),on='cust_id')
        
        
        df['tran_date_day_name'] = df['tran_date'].dt.weekday.map({0: 'Monday',
                                                              1: 'Tuesday',
                                                              2: 'Wednesday',
                                                              3: 'Thursday',
                                                              4: 'Friday',
                                                              5: 'Saturday',
                                                              6: 'Sunday'})
        
        self.merged = df

        
        
df = db()
df.merge()

# we create the basic layout of the dashboard of two tabs: 'Sales in total' and 'Products'.
# we initialize the application, additionally using the 'external_stylesheet'
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets,suppress_callback_exceptions=True)

app.layout = html.Div([html.Div([dcc.Tabs(id='tabs',value='tab-1',children=[
                            dcc.Tab(label='Sales in total',value='tab-1'),
                            dcc.Tab(label='Products',value='tab-2'),
                            dcc.Tab(label='Sales channels',value='tab-3'),
                            dcc.Tab(label='Customers',value='tab-4'),
                            ]),
                            html.Div(id='tabs-content')
                    ],style={'width':'80%','margin':'auto'})],
                    style={'height':'100%'})

@app.callback(Output('tabs-content','children'),[Input('tabs','value')])
def render_content(tab):
    """rendering the contents of the active tab"""
    if tab == 'tab-1':
        return tab1.render_tab(df.merged)
    elif tab == 'tab-2':
        return tab2.render_tab(df.merged)
    elif tab == 'tab-3':
        return tab3.render_tab(df.merged)
    elif tab == 'tab-4':
        return tab4.render_tab(df.merged)
    
## tab1 callbacks
@app.callback(Output('bar-sales','figure'),
    [Input('sales-range','start_date'),Input('sales-range','end_date')])

def tab1_bar_sales(start_date,end_date):
    """
    create the tab1_bar_sales function,
    we narrow down the DataFrame with transactions based on the dates selected by the user, 
    generate a chart
    """
    truncated = df.merged[(df.merged['tran_date']>=start_date)&(df.merged['tran_date']<=end_date)]
    grouped = truncated[truncated['total_amt']>0].groupby([pd.Grouper(key='tran_date',freq='M'),'Store_type'])['total_amt'].sum().round(2).unstack()

    traces = []
    for col in grouped.columns:
        traces.append(go.Bar(x=grouped.index,y=grouped[col],name=col,hoverinfo='text',
        hovertext=[f'{y/1e3:.2f}k' for y in grouped[col].values]))

    data = traces
    fig = go.Figure(data=data,layout=go.Layout(title='Revenue',barmode='stack',legend=dict(x=0,y=-0.5)))

    return fig

@app.callback(Output('choropleth-sales','figure'),
            [Input('sales-range','start_date'),Input('sales-range','end_date')])
def tab1_choropleth_sales(start_date,end_date):
    """we create a cartogram with the level of sales by country"""
    truncated = df.merged[(df.merged['tran_date']>=start_date)&(df.merged['tran_date']<=end_date)]
    grouped = truncated[truncated['total_amt']>0].groupby('country')['total_amt'].sum().round(2)

    trace0 = go.Choropleth(colorscale='Viridis',reversescale=True,
                            locations=grouped.index,locationmode='country names',
                            z = grouped.values, colorbar=dict(title='Sales'))
    data = [trace0]
    fig = go.Figure(data=data,layout=go.Layout(title='Map',geo=dict(showframe=False,projection={'type':'natural earth'})))

    return fig

## tab2 callbacks
@app.callback(Output('barh-prod-subcat','figure'),
            [Input('prod_dropdown','value')])

def tab2_barh_prod_subcat(chosen_cat):
    """we create a callback responsible for generating a horizontal bar chart"""
    grouped = df.merged[(df.merged['total_amt']>0)&(df.merged['prod_cat']==chosen_cat)].pivot_table(index='prod_subcat',columns='Gender',values='total_amt',aggfunc='sum').assign(_sum=lambda x: x['F']+x['M']).sort_values(by='_sum').round(2)

    traces = []
    for col in ['F','M']:
        traces.append(go.Bar(x=grouped[col],y=grouped.index,orientation='h',name=col))

    data = traces
    fig = go.Figure(data=data,layout=go.Layout(barmode='stack',margin={'t':20,}))
    return fig

## tab3 callbacks
@app.callback(Output('pie-store-type','figure'), [Input('store_dropdown','value')])
def tab3_pie_store_type(chosen_cat):
    """we create pie chart for the sales by Store_type and day of week"""
    grouped = df.merged[df.merged['total_amt']>0].groupby(['Store_type','tran_date_day_name'])['total_amt'].sum()
    grouped_store = grouped[chosen_cat]
    fig = go.Figure(data=[go.Pie(labels=grouped_store.index,values=grouped_store.values)],layout=go.Layout(title='by sales channels'))
    return fig

@app.callback(Output('pie-day','figure'), [Input('day_dropdown','value')])
def tab3_pie_day(chosen_cat):

    grouped = df.merged[df.merged['total_amt']>0].groupby(['tran_date_day_name','Store_type'])['total_amt'].sum()
    grouped_day = grouped[chosen_cat]
    fig = go.Figure(data=[go.Pie(labels=grouped_day.index,values=grouped_day.values)],layout=go.Layout(title='by day of week'))
    return fig

## tab4 callbacks
@app.callback(Output('pie-gender','figure'), [Input('store_dropdown_gender','value')])
def tab4_pie_gender(chosen_cat):
    """we create py chart for the sales by Store_type and gander"""
    grouped = df.merged[df.merged['total_amt']>0].groupby(['Store_type','Gender'])['total_amt'].sum()
    grouped_gender = grouped[chosen_cat]
    fig = go.Figure(data=[go.Pie(labels=grouped_gender.index,values=grouped_gender.values)],layout=go.Layout(title='by gender'))
    return fig

@app.callback(Output('pie-country','figure'), [Input('store_dropdown_country','value')])
def tab4_pie_country(chosen_cat):
    """we create pie chart for the sales by Store_type and country"""
    grouped = df.merged[df.merged['total_amt']>0].groupby(['Store_type','country'])['total_amt'].sum()
    grouped_country = grouped[chosen_cat]
    fig = go.Figure(data=[go.Pie(labels=grouped_country.index,values=grouped_country.values)],layout=go.Layout(title='by country'))
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)


