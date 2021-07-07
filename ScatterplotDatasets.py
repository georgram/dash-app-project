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
df= pd.read_csv("Circular44_dataframe edited.csv")


layout = html.Div([
    html.Div([

        html.Div([
            dcc.Dropdown(
                id='xaxis-column',
                options=[
                    {'label': '% of pop eating meat <1 a week', 'value': 'meat<=1(o)'},
                    {'label': 'short chain importance(o)', 'value': 'short chain importance(o)'},
                    {'label': 'info available(o)', 'value': 'info available(o)'},
                    {'label': 'use renewable energy(o)', 'value': 'use renewable energy(o)'},
                    {'label': 'replan energy use(o)', 'value': 'replan energy use(o)'},
                    {'label': 'Redesign(o)', 'value': 'Redesign(o)'},

                    {'label': 'funding awareness(o)', 'value': 'funding awareness(o)'},
                    {'label': 'Circular company actions(o)', 'value': 'Circular company actions(o)'},
                    {'label': 'easy to eat healthy(o)', 'value': 'easy to eat healthy(o)'},
                    {'label': 'pop density', 'value': 'pop density'},
                    {'label': 'obesity', 'value': 'obesity'},
                    {'label': 'perceived health(o)', 'value': 'perceived health(o)'},

                    {'label': 'median age', 'value': 'median'},
                    {'label': 'Population', 'value': 'Population'},
                    {'label': 'Self suffeciency importance(o)', 'value': 'Self suffeciency importance(o)'},
                    {'label': 'origin importance(o)', 'value': 'origin importance(o)'},
                    {'label': 'importance of qlty(o)', 'value': 'importance of qlty(o)'},
                    {'label': 'self blame for waste', 'value': 'self blame(o)'},

                    {'label': 'rail infrastructure', 'value': 'rail infrastructure'},
                    {'label': 'inland water transport', 'value': 'inland water transport'},
                    {'label': 'road 2000 6000', 'value': 'road 2000 6000'},
                    {'label': 'road 500 2000', 'value': 'road 500 2000'},
                    {'label': 'road 300 500', 'value': 'road 300 500'},
                    {'label': 'road 150 300', 'value': 'road 150 300'},

                    {'label': 'road 50 150', 'value': 'road 50 150'},
                    {'label': 'road 0 50', 'value': 'road 0 50'},
                    {'label': 'road food transport', 'value': 'road food transport'},
                    {'label': 'rail food transport', 'value': 'rail food transport'},
                    {'label': 'agr emissions', 'value': 'agr emissions'},
                    {'label': 'fertilizer sales', 'value': 'fertilizer sales'},

                    {'label': 'pesticide sales', 'value': 'pesticide sales'},
                    {'label': 'Processors(I)', 'value': 'Processors(I)'},
                    {'label': 'Agr producers', 'value': 'Agr producers'},
                    {'label': 'Exporters(I)', 'value': 'Exporters(I)'},
                    {'label': 'Importers', 'value': 'Importers'},
                    {'label': 'per_1000_Crop_production', 'value': 'per_1000_Crop_production'},

                    {'label': 'per_1000_Farm_Trained_Staff', 'value': 'per_1000_Farm_Trained_Staff'},
                    {'label': 'per_1000_kitchen_gardens', 'value': 'per_1000_kitchen_gardens'},
                    {'label': 'organic farming percentage', 'value': 'organic farming percentage'},
                    {'label': 'Recycling rate of municipal waste', 'value': 'Recycling rate of municipal waste'},
                    {'label': 'investments on c.e. per gdp', 'value': 'investments per gdp'},
                    {'label': 'municipal waste per capita', 'value': 'municipal_waste_per_capita'},

                    {'label': 'GDP per capita', 'value': 'GDP per capita'},
                    {'label': 'Recycling rate of packaging', 'value': 'Recycling rate of packaging'},
                    {'label': 'Recycled biowaste per capita', 'value': 'Recycled biowaste per capita'},
                ],
                value="municipal_waste_per_capita"
            ),
            dcc.RadioItems(
                id='xaxis-type',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle={'display': 'inline-block'}
            )
        ],
        style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                id='yaxis-column',
                options=[
                         {'label': '% of pop eating meat <1 a week', 'value': 'meat<=1(o)'},
                         {'label': 'short chain importance(o)', 'value': 'short chain importance(o)'},
                         {'label': 'info available(o)', 'value': 'info available(o)'},
                         {'label': 'use renewable energy(o)', 'value': 'use renewable energy(o)'},
                         {'label': 'replan energy use(o)', 'value': 'replan energy use(o)'},
                         {'label': 'Redesign(o)', 'value': 'Redesign(o)'},

                         {'label': 'funding awareness(o)', 'value': 'funding awareness(o)'},
                         {'label': 'Circular company actions(o)', 'value': 'Circular company actions(o)'},
                         {'label': 'easy to eat healthy(o)', 'value': 'easy to eat healthy(o)'},
                         {'label': 'pop density', 'value': 'pop density'},
                         {'label': 'obesity', 'value': 'obesity'},
                         {'label': 'perceived health(o)', 'value': 'perceived health(o)'},

                         {'label': 'median age', 'value': 'median'},
                         {'label': 'Population', 'value': 'Population'},
                         {'label': 'Self suffeciency importance(o)', 'value': 'Self suffeciency importance(o)'},
                         {'label': 'origin importance(o)', 'value': 'origin importance(o)'},
                         {'label': 'importance of qlty(o)', 'value': 'importance of qlty(o)'},
                         {'label': 'self blame for waste', 'value': 'self blame(o)'},

                         {'label': 'rail infrastructure', 'value': 'rail infrastructure'},
                         {'label': 'inland water transport', 'value': 'inland water transport'},
                         {'label': 'road 2000 6000', 'value': 'road 2000 6000'},
                         {'label': 'road 500 2000', 'value': 'road 500 2000'},
                         {'label': 'road 300 500', 'value': 'road 300 500'},
                         {'label': 'road 150 300', 'value': 'road 150 300'},

                         {'label': 'road 50 150', 'value': 'road 50 150'},
                         {'label': 'road 0 50', 'value': 'road 0 50'},
                         {'label': 'road food transport', 'value': 'road food transport'},
                         {'label': 'rail food transport', 'value': 'rail food transport'},
                         {'label': 'agr emissions', 'value': 'agr emissions'},
                         {'label': 'fertilizer sales', 'value': 'fertilizer sales'},

                         {'label': 'pesticide sales', 'value': 'pesticide sales'},
                         {'label': 'Processors(I)', 'value': 'Processors(I)'},
                         {'label': 'Agr producers', 'value': 'Agr producers'},
                         {'label': 'Exporters(I)', 'value': 'Exporters(I)'},
                         {'label': 'Importers', 'value': 'Importers'},
                         {'label': 'per_1000_Crop_production', 'value': 'per_1000_Crop_production'},

                         {'label': 'per_1000_Farm_Trained_Staff', 'value': 'per_1000_Farm_Trained_Staff'},
                         {'label': 'per_1000_kitchen_gardens', 'value': 'per_1000_kitchen_gardens'},
                         {'label': 'organic farming percentage', 'value': 'organic farming percentage'},
                         {'label': 'Recycling rate of municipal waste', 'value': 'Recycling rate of municipal waste'},
                         {'label': 'investments on c.e. per gdp', 'value': 'investments per gdp'},
                         {'label': 'municipal waste per capita', 'value': 'municipal_waste_per_capita'},

                         {'label': 'GDP per capita', 'value': 'GDP per capita'},
                         {'label': 'Recycling rate of packaging', 'value': 'Recycling rate of packaging'},
                         {'label': 'Recycled biowaste per capita', 'value': 'Recycled biowaste per capita'},
                     ],
                value='Recycling rate of municipal waste'
            ),
            dcc.RadioItems(
                id='yaxis-type',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle={'display': 'inline-block'}
            )
        ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),

    dcc.Graph(id='indicator-graphic'),


])

@app.callback(
    Output('indicator-graphic', 'figure'),
    Input('xaxis-column', 'value'),
    Input('yaxis-column', 'value'),
    Input('xaxis-type', 'value'),
    Input('yaxis-type', 'value'))

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






