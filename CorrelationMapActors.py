import pandas as pd  # (version 1.0.0)
import plotly  # (version 4.5.4) pip install plotly==4.5.4
import plotly.express as px

import dash  # (version 1.9.1) pip install dash==1.9.1
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from app import app



# ---------------------------------------------------------------
# Taken from https://opendata.cityofnewyork.us/
df= pd.read_csv("GroupedByActorsFinal.csv")

# ---------------------------------------------------------------
layout = html.Div([

    html.Div([
        dcc.Graph(id='our_graph_CorrelationMapActors')
    ], className='nine columns'),

    html.Div([

        html.Br(),
        html.Div(id='output_data_CorrelationMapActors'),
        html.Br(),

        html.Label(['Choose column:'], style={'font-weight': 'bold', "text-align": "center"}),

        dcc.Dropdown(id='my_dropdown_CorrelationMapActors',
                     options=[
                         {'label': 'Assets and Resources Score', 'value': 'Assets and Resources Score'},
                         {'label': 'Actors and Stakeholders Score', 'value': 'Actors and Stakeholders Score'},
                         {'label': 'Flows and Processes Score', 'value': 'Flows and Processes Score'},
                         {'label': 'Systems and Enviroments Score', 'value': 'Systems and Enviroments Score'}
                     ],
                     optionHeight=35,  # height/space between dropdown options
                     value='Assets and Resources Score',  # dropdown value selected automatically when page loads
                     disabled=False,  # disable dropdown value selection
                     multi=False,  # allow multiple dropdown values to be selected
                     searchable=True,  # allow user-searching of dropdown values
                     search_value='',  # remembers the value searched in dropdown
                     placeholder='Please select...',  # gray, default text shown when no option is selected
                     clearable=True,  # allow user to removes the selected value
                     style={'width': "100%"},  # use dictionary to define CSS styles of your dropdown
                     # className='select_box',           #activate separate CSS document in assets folder
                     # persistence=True,                 #remembers dropdown value. Used with persistence_type
                     # persistence_type='memory'         #remembers dropdown value selected until...
                     ),  # 'memory': browser tab is refreshed
        # 'session': browser tab is closed
        # 'local': browser cookies are deleted
    ], className='three columns'),

])


# ---------------------------------------------------------------
# Connecting the Dropdown values to the graph
@app.callback(
    Output(component_id='our_graph_CorrelationMapActors', component_property='figure'),
    [Input(component_id='my_dropdown_CorrelationMapActors', component_property='value')]
)
def build_graph(column_chosen):
    df.sort_values(column_chosen, ascending=True, inplace=True)
    fig = px.choropleth(df, locations="Country",
                        color=column_chosen,
                        hover_name="Country",
                        projection='natural earth',
                        scope='europe',
                        locationmode='ISO-3',
                        title=column_chosen,
                        color_continuous_scale=px.colors.sequential.YlOrRd)
    fig = go.Figure(data=go.Choropleth(
        locations=df['Country'],
        z=df[column_chosen],
        colorscale='Reds',
        text=df['Country'],  # hover text
    ))

    fig = px.bar(df, y='Country', x=column_chosen,height=1000, width=800)

    #fig.update_layout(title=dict(font=dict(size=28), x=0.5, xanchor='center'),
                     # margin=dict(l=60, r=60, t=50, b=50))
    corrMatrix = df.corr()
    fig = px.imshow(corrMatrix,height=1200, width=1200)
    return fig


# ---------------------------------------------------------------
# For tutorial purposes to show the user the search_value

@app.callback(
    Output(component_id='output_data_CorrelationMapActors', component_property='children'),
    [Input(component_id='my_dropdown_CorrelationMapActors', component_property='search_value')]
)
def build_graph(data_chosen):
    return (' {} '.format(data_chosen))


# ---------------------------------------------------------------
