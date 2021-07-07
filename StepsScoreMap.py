import pandas as pd  # (version 1.0.0)
import plotly  # (version 4.5.4) pip install plotly==4.5.4
import plotly.express as px

import dash  # (version 1.9.1) pip install dash==1.9.1
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from app import app

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# ---------------------------------------------------------------
# Taken from https://opendata.cityofnewyork.us/
df= pd.read_csv("GroupedByStepFinal.csv")

# ---------------------------------------------------------------
layout = html.Div([

    html.Div([
        dcc.Graph(id='our_graph_Steps_Score_Map')
    ]),

    html.Div([

        html.Br(),
        html.Div(id='output_data_Steps_Score_Map'),
        html.Br(),
        html.Div(id='sentence_output_Steps_Score_Map'),

        html.Label(['Choose Dataset:'], style={'font-weight': 'bold', "text-align": "center"}),

        dcc.Dropdown(id='my_dropdown_Steps_Score_Map',
                     options=[
                         {'label': 'Production Score', 'value': 'Production Score'},
                         {'label': 'Processing Score', 'value': 'Processing Score'},
                         {'label': 'Distribution Score', 'value': 'Distribution Score'},
                         {'label': 'Consumption Score', 'value': 'Consumption Score'},
                         {'label': 'WasteManagment Score', 'value': 'WasteManagment Score'},
                         {'label': 'Overal Score', 'value': 'Overal Score'},

                     ],
                     optionHeight=35,  # height/space between dropdown options
                     value='Overal Score',  # dropdown value selected automatically when page loads
                     disabled=False,  # disable dropdown value selection
                     multi=False,  # allow multiple dropdown values to be selected
                     searchable=True,  # allow user-searching of dropdown values
                     search_value='',  # remembers the value searched in dropdown
                     placeholder='Please select...',  # gray, default text shown when no option is selected
                     clearable=True,  # allow user to removes the selected value
                     style={'width': "100%",'font-weight': 'bold', "text-align": "center"},  # use dictionary to define CSS styles of your dropdown
                     # className='select_box',           #activate separate CSS document in assets folder
                     # persistence=True,                 #remembers dropdown value. Used with persistence_type
                     # persistence_type='memory'         #remembers dropdown value selected until...
                     ),  # 'memory': browser tab is refreshed
        # 'session': browser tab is closed
        # 'local': browser cookies are deleted

    ], ),

])


# ---------------------------------------------------------------
# Connecting the Dropdown values to the graph

@app.callback(
    [Output(component_id='our_graph_Steps_Score_Map', component_property='figure'), Output('sentence_output_Steps_Score_Map', 'children')],
    [Input(component_id='my_dropdown_Steps_Score_Map', component_property='value'),
     Input(component_id='my_dropdown_Steps_Score_Map', component_property='value')],
    prevent_initial_call=False
)

def build_graph(column_chosen,text):

    fig = go.Figure(data=go.Choropleth(
        locations=df['Country'],
        z=df[column_chosen],
        colorscale=px.colors.sequential.YlOrRd,
        text=df['Country']# hover text
    ))

    fig.update_layout(title=dict(font=dict(size=28), x=0.5, xanchor='center',yanchor='middle',text=column_chosen),
                      margin=dict(l=20, r=20, t=40, b=0),autosize=False,width=1300,height=650)
    fig.update_geos(scope='europe')
    df.sort_values(column_chosen, ascending=True, inplace=True)
    last_country=str(df['Country'].iloc[0])
    lcountry_number=str(format(float(df[column_chosen].iloc[0]),".2f"))
    df.sort_values(column_chosen, ascending=False, inplace=True)
    first_country = str(df['Country'].iloc[0])
    fcountry_number = str(format(float(df[column_chosen].iloc[0]),".2f"))
    average=str(format(float(df[column_chosen].mean()),".2f"))
    std=str(format(float(df[column_chosen].std()),".2f"))
    #print(str(country_number))

    text=("The european country ranking lowest in "+ column_chosen +" is "+ last_country +" with a score of "+ lcountry_number+" ."
          " The european country ranking highest in "+ column_chosen +" is "+ first_country +" with a score of "+ fcountry_number+" ."
          "The european average is "+average+". with a standard deviation of "+std+". ")

    #text="e"


    return (fig,(text+'For more information on the {} dataset visit: https://docs.google.com/presentation/d/1VnBta-IN2cIyuAfuCuU0z0zZrz3XkXwEaysJgokM9lA/edit?usp=sharing'.format(column_chosen)))





