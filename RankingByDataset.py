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
df= pd.read_csv("Circular44_dataframe edited.csv")

# ---------------------------------------------------------------
layout = html.Div([

    html.Div([
        dcc.Graph(id='our_graph')
    ]),

    html.Div([

        html.Br(),
        html.Div(id='output_data'),
        html.Br(),
        html.Div(id='sentence_output'),

        html.Label(['Choose Dataset:'], style={'font-weight': 'bold', "text-align": "center"}),

        dcc.Dropdown(id='my_dropdown',
                     options=[
                         {'label': '% of pop eating meat <1 a week', 'value': 'meat<=1(o)'},
                         {'label': 'short supply chain importance(o) for consumers', 'value': 'short chain importance(o)'},
                         {'label': 'information available to companies about Circular economy(o)', 'value': 'info available(o)'},
                         {'label': 'use renewable energy by companies(o)', 'value': 'use renewable energy(o)'},
                         {'label': 'Companies that replanned their energy use this decade(o)', 'value': 'replan energy use(o)'},
                         {'label': 'Companies that Redesigned their products for circularity this decade (o)', 'value': 'Redesign(o)'},

                         {'label': 'Companies aware of circular economy funding(o)', 'value': 'funding awareness(o)'},
                         {'label': 'Companies taking action to become more circular(o)', 'value': 'Circular company actions(o)'},
                         {'label': 'Citizens reporting it is easy to eat healthy(o)', 'value': 'easy to eat healthy(o)'},
                         {'label': 'Population density', 'value': 'pop density'},
                         {'label': 'obesity percentage', 'value': 'obesity'},
                         {'label': 'perceived health by citizen(o)', 'value': 'perceived health(o)'},

                         {'label': 'median age', 'value': 'median'},
                         {'label': 'Population', 'value': 'Population'},
                         {'label': 'Self suffeciency importance for citizens(o)', 'value': 'Self suffeciency importance(o)'},
                         {'label': 'Importance of food origin for citizens (o)', 'value': 'origin importance(o)'},
                         {'label': 'importance of food quality(o)', 'value': 'importance of qlty(o)'},
                         {'label': 'Citizens blaming their self for waste problem', 'value': 'self blame(o)'},

                         {'label': 'rail infrastructure', 'value': 'rail infrastructure'},
                         {'label': 'inland water transport', 'value': 'inland water transport'},
                         {'label': 'Food transported for 2000 to 6000 kilometers', 'value': 'road 2000 6000'},
                         {'label': 'Food transported 500 to 2000 kilometers', 'value': 'road 500 2000'},
                         {'label': 'Food transported 300 to 500 kilometers', 'value': 'road 300 500'},
                         {'label': 'Food transported 150 to 300 kilometers', 'value': 'road 150 300'},

                         {'label': 'Food transported 50 to 150 kilometers', 'value': 'road 50 150'},
                         {'label': 'Food transported 0 to 50 kilometers', 'value': 'road 0 50'},
                         {'label': 'road food transport', 'value': 'road food transport'},
                         {'label': 'rail food transport', 'value': 'rail food transport'},
                         {'label': 'agricultural emissions', 'value': 'agr emissions'},
                         {'label': 'fertilizer sales', 'value': 'fertilizer sales'},

                         {'label': 'pesticide sales', 'value': 'pesticide sales'},
                         {'label': 'Processors(I)', 'value': 'Processors(I)'},
                         {'label': 'Agricultural producers', 'value': 'Agr producers'},
                         {'label': 'Exporters(I)', 'value': 'Exporters(I)'},
                         {'label': 'Importers', 'value': 'Importers'},
                         {'label': 'Crop production per 1000 citizens', 'value': 'per_1000_Crop_production'},

                         {'label': 'Farm trained stuff per 1000 citizens', 'value': 'per_1000_Farm_Trained_Staff'},
                         {'label': 'Kitchen gardens per 1000 citizens', 'value': 'per_1000_kitchen_gardens'},
                         {'label': 'organic farming percentage', 'value': 'organic farming percentage'},
                         {'label': 'Recycling rate of municipal waste', 'value': 'Recycling rate of municipal waste'},
                         {'label': 'investments on circular economy per gdp', 'value': 'investments per gdp'},
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
    [Output(component_id='our_graph', component_property='figure'), Output('sentence_output', 'children')],
    [Input(component_id='my_dropdown', component_property='value'),
     Input(component_id='my_dropdown', component_property='value')],
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


