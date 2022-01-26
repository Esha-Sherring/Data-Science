# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 00:58:24 2022

@author: esher
"""

import numpy as np
import pandas as pd
import plotly.express as px


import dash
import dash_core_components as dcc
import dash_html_components as html
colorscales = px.colors.named_colorscales()

df = pd.read_csv('WHO-COVID-19-global-table-data.csv') 
df['Country']=df.index
df=df.drop(['Name'],axis=1)



#External CSS file for the python dashboard
#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#Initializing a dash application
app = dash.Dash(__name__)

header = html.H1(children="Covid-19 cases in India Data Anyalisis", style={"textAlign": "center","backgroundColor":"#80e5ff","font-family": 'Trebuchet MS',"padding":"3%","fontSize":"3rem","marginTop":"0"})
rowbartotal = html.H3(children=["Cumilative total in different countires"],style={"textAlign": "center","color":"red","font-family": "Times New Roman"})
c1= px.bar(df.head(15), x = 'Country', y = 'Cases - cumulative total',
                        color='Cases - cumulative total',     
                               color_continuous_scale='viridis',
           height = 500,
       hover_data = ['Country', 'Cases - cumulative total'])


g1 = dcc.Graph(
        id='g1',
        figure=c1,
        className="six columns"
    )
row1=html.Div(children=[g1])
layout = html.Div(children=[header,rowbartotal,row1])

app.layout = layout

#running the dashboard application on the local browser
#Dash will run on http://127.0.0.1:8050/
if __name__ == "__main__":
    app.run_server(debug=True)
