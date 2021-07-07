import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

# must add this line in order for the app to be deployed successfully on Heroku
from app import server
from app import app
# import all pages in the app
from apps import ActorsScoreMap,CorrelationMapActors,ScatterplotSteps,StepsScoreBars,StepsScoreMap,CorrelationMapSteps,global_situation, singapore, home, RankingByDataset, ScatterplotDatasets, CorrelationMapDatasets, RankingByDatasetBars, PairCorrelationRankings, NegativePairCorrelationRankings

# building the navigation bar
# https://github.com/facultyai/dash-bootstrap-components/blob/master/examples/advanced-component-usage/Navbars.py
dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Home", href="/home"),
        #dbc.DropdownMenuItem("Global", href="global_situation"),
        #dbc.DropdownMenuItem("Singapore", href="/singapore"),
        dbc.DropdownMenuItem("ScatterplotDatasets", href="ScatterplotDatasets"),
        dbc.DropdownMenuItem("RankingByDataset", href="RankingByDataset"),
        dbc.DropdownMenuItem("CorrelationMapDatasets", href="CorrelationMapDatasets"),
        dbc.DropdownMenuItem("RankingByDatasetBars", href="RankingByDatasetBars"),
        dbc.DropdownMenuItem("PairCorrelationRankings", href="PairCorrelationRankings"),
        dbc.DropdownMenuItem("NegativePairCorrelationRankings", href="NegativePairCorrelationRankings"),
        dbc.DropdownMenuItem("CorrelationMapSteps", href="CorrelationMapSteps"),
        dbc.DropdownMenuItem("StepsScoreMap", href="StepsScoreMap"),
        dbc.DropdownMenuItem("StepsScoreBars", href="StepsScoreBars"),
        dbc.DropdownMenuItem("ActorsScoreMap", href="ActorsScoreMap"),
        dbc.DropdownMenuItem("Scatterplotsteps", href="ScatterplotSteps"),
        dbc.DropdownMenuItem("CorrelationMapActors", href="CorrelationMapActors")

    ],
    nav = True,
    in_navbar = True,
    label = "Explore",
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="/assets/recycle symbol.png", height="30px")),
                        dbc.Col(dbc.NavbarBrand("OPEN EU DATA ON CIRCULAR ECONOMY", className="ml-2")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="/home",
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    # right align dropdown menu with ml-auto className
                    [dropdown], className="ml-auto", navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
    className="mb-4",
)

def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

for i in [2]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)

# embedding the navigation bar
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/global_situation':
        return global_situation.layout
    elif pathname == '/singapore':
        return singapore.layout
    elif pathname == '/RankingByDataset':
        return RankingByDataset.layout
    elif pathname == '/ScatterplotDatasets':
        return ScatterplotDatasets.layout
    elif pathname == '/CorrelationMapDatasets':
        return CorrelationMapDatasets.layout
    elif pathname == '/RankingByDatasetBars':
        return RankingByDatasetBars.layout
    elif pathname == '/PairCorrelationRankings':
        return PairCorrelationRankings.layout
    elif pathname == '/NegativePairCorrelationRankings':
        return NegativePairCorrelationRankings.layout
    elif pathname == '/CorrelationMapSteps':
        return CorrelationMapSteps.layout
    elif pathname == '/StepsScoreMap':
        return StepsScoreMap.layout
    elif pathname == '/StepsScoreBars':
        return StepsScoreBars.layout
    elif pathname == '/ActorsScoreMap':
        return ActorsScoreMap.layout
    elif pathname == '/ScatterplotSteps':
        return ScatterplotSteps.layout
    elif pathname == '/CorrelationMapActors':
        return CorrelationMapActors.layout
    else:
        return home.layout

if __name__ == '__main__':
    app.run_server(debug=True)