import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
from scipy.stats import pearsonr

import pandas as pd
from app import app

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#df = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')
df= pd.read_csv("GroupedByStepFinal.csv")


layout = html.Div([
    html.Div([

        html.Div([
            dcc.Dropdown(
                id='xaxis-column_ScatterplotSteps',
                options=[
                    {'label': 'Production Score', 'value': 'Production Score'},
                    {'label': 'Processing Score', 'value': 'Processing Score'},
                    {'label': 'Distribution Score', 'value': 'Distribution Score'},
                    {'label': 'Consumption Score', 'value': 'Consumption Score'},
                    {'label': 'WasteManagement Score', 'value': 'WasteManagment Score'},
                    {'label': 'Overal Score', 'value': 'Overal Score'}

                ],
                value="Production Score"
            ),
            dcc.RadioItems(
                id='xaxis-type_ScatterplotSteps',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle={'display': 'inline-block'}
            )
        ],
        style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                id='yaxis-column_ScatterplotSteps',
                options=[
                    {'label': 'Production Score', 'value': 'Production Score'},
                    {'label': 'Processing Score', 'value': 'Processing Score'},
                    {'label': 'Distribution Score', 'value': 'Distribution Score'},
                    {'label': 'Consumption Score', 'value': 'Consumption Score'},
                    {'label': 'WasteManagement Score', 'value': 'WasteManagment Score'},
                    {'label': 'Overal Score', 'value': 'Overal Score'}
                     ],
                value='Overal Score'
            ),
            dcc.RadioItems(
                id='yaxis-type_ScatterplotSteps',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle={'display': 'inline-block'}
            )
        ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),

    dcc.Graph(id='indicator-graphic_ScatterplotSteps'),


])

@app.callback(
    Output('indicator-graphic_ScatterplotSteps', 'figure'),
    Input('xaxis-column_ScatterplotSteps', 'value'),
    Input('yaxis-column_ScatterplotSteps', 'value'),
    Input('xaxis-type_ScatterplotSteps', 'value'),
    Input('yaxis-type_ScatterplotSteps', 'value'))

def update_graph(xaxis_column_name, yaxis_column_name,
                 xaxis_type, yaxis_type):
    dat=df.corr(method="pearson")
    pearson=str(format(float(dat.loc[xaxis_column_name][yaxis_column_name]),'.3f'))

    dat=df.corr(method='kendall')
    kendal=str(format(float(dat.loc[xaxis_column_name][yaxis_column_name]),'.3f'))
    dat = df.corr(method='spearman')
    spearman =str(format(float(dat.loc[xaxis_column_name][yaxis_column_name]),'.3f'))
    text=("Pearson: "+pearson+" Kendall: "+kendal+" Spearman: "+spearman+" ")

    #data1.fillna(inplace=True,value='scalar')
    #data2.fillna(inplace=True,value='scalar')



    fig = px.scatter(df,x=xaxis_column_name,y=yaxis_column_name,
                     hover_name='Country',trendline='ols')

    fig.update_layout(margin={'l': 40, 'b': 40, 't': 60, 'r': 0}, hovermode='closest',title=text)

    fig.update_xaxes(title=xaxis_column_name,
                     type='linear' if xaxis_type == 'Linear' else 'log')

    fig.update_yaxes(title=yaxis_column_name,
                     type='linear' if yaxis_type == 'Linear' else 'log')

    return fig




