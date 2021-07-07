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
df= pd.read_csv("Circular44_nswe_editedFinal.csv")

# ---------------------------------------------------------------
layout = html.Div([

    html.Div([
        dcc.Graph(id='our_graph_RankingByDatasetBars')
    ], className='nine columns'),

    html.Div([

        html.Br(),
        html.Div(id='output_data_RankingByDatasetBars'),
        html.Br(),

        html.Label(['Choose column:'], style={'font-weight': 'bold', "text-align": "center"}),

        dcc.Dropdown(id='my_dropdown',
                     options=[
                         {'label': '% of pop eating meat <1 a week', 'value': 'meat consumption less than 1/wk'},
                         {'label': 'short chain importance to consumers(o)', 'value': 'short chain importance(o)'},
                         {'label': 'circular info available to companies (o)', 'value': 'circular info available(o)'},
                         {'label': 'use renewable energy(o)', 'value': 'using renewable energy(o)'},
                         {'label': 'replan energy use(o)', 'value': 'companies replaning energy use(o)'},
                         {'label': 'Redesign(o)', 'value': 'companies Redesigning products(o)'},

                         {'label': 'funding awareness(o)', 'value': 'funding awareness(o)'},
                         {'label': 'Circular company actions(o)', 'value': 'Circular company actions(o)'},
                         {'label': 'easy to eat healthy(o)', 'value': 'easy to eat healthy(o)'},
                         {'label': 'pop density', 'value': 'pop density'},
                         {'label': 'obesity', 'value': 'obesity'},
                         {'label': 'perceived health(o)', 'value': 'perceived health(o)'},

                         {'label': 'median age', 'value': 'median'},
                         {'label': 'Population', 'value': 'Population'},
                         {'label': 'Self suffeciency importance(o)', 'value': 'Self suffeciency importance(o)'},
                         {'label': 'importance(o) of food origin', 'value': 'importance(o) of food origin'},
                         {'label': 'importance of food qlty(o)', 'value': 'importance of food qlty(o)'},
                         {'label': 'self blame for food waste', 'value': 'self blame for food waste(o)'},

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
                     optionHeight=35,  # height/space between dropdown options
                     value='obesity',  # dropdown value selected automatically when page loads
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
    Output(component_id='our_graph_RankingByDatasetBars', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]
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
    return fig


# ---------------------------------------------------------------
# For tutorial purposes to show the user the search_value

@app.callback(
    Output(component_id='output_data_RankingByDatasetBars', component_property='children'),
    [Input(component_id='my_dropdown', component_property='search_value')]
)
def build_graph(data_chosen):
    return (' {} '.format(data_chosen))


# ---------------------------------------------------------------



