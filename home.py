import dash_html_components as html
import dash_bootstrap_components as dbc

# needed only if running this as a single page app
#external_stylesheets = [dbc.themes.LUX]

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# change to app.layout if running as single page app instead
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Welcome to the circular economy Framework", className="text-center")
                    , className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(html.H5(children='This simple and easy to use interactive framework is here to allow you to visualise, analyse and understand open data on the circular economy of europe! '
                                     )
                    , className="mb-4")
            ]),

        dbc.Row([
            dbc.Col(html.H5(children='In the cards bellow you can find more information about our project and why its important. By clicking the dropdown menu on the top right of your screen you can start exploring the visualisations of the data. ')
                    , className="mb-5")
        ]),

        dbc.Row([
            dbc.Col(dbc.Card(children=[html.H3(children='Get information on the dataset and the issue of farm to fork',
                                               className="text-center"),
                                       dbc.Row([dbc.Col(dbc.Button("Farm to Fork", href="https://ec.europa.eu/info/strategy/priorities-2019-2024/european-green-deal/actions-being-taken-eu/farm-fork_en",
                                                                   color="primary"),
                                                        className="mt-3"),
                                                dbc.Col(dbc.Button("Datasets", href="https://docs.google.com/presentation/d/1VnBta-IN2cIyuAfuCuU0z0zZrz3XkXwEaysJgokM9lA/edit?usp=sharing",
                                                                   color="primary"),
                                                        className="mt-3")], justify="center")
                                       ],
                             body=True, color="dark", outline=True)
                    , width=4, className="mb-4"),

            dbc.Col(dbc.Card(children=[html.H3(children='Access the code used to build this dashboard',
                                               className="text-center"),
                                       dbc.Button("GitHub",
                                                  href="https://drive.google.com/drive/folders/1iQzqAF6j5erFxndCa3jmVnO_s4Jvt_1n?usp=sharing",
                                                  color="primary",
                                                  className="mt-3"),
                                       ],
                             body=True, color="dark", outline=True)
                    , width=4, className="mb-4"),

            dbc.Col(dbc.Card(children=[html.H3(children='Read the thesis paper',
                                               className="text-center"),
                                       dbc.Button("Thesis pdf",
                                                  href="https://drive.google.com/drive/folders/1iQzqAF6j5erFxndCa3jmVnO_s4Jvt_1n?usp=sharing",
                                                  color="primary",
                                                  className="mt-3"),

                                       ],
                             body=True, color="dark", outline=True)
                    , width=4, className="mb-4")
        ], className="mb-5"),

        html.A("For any suggestions, inquiries and ideas we would be happy to hear from you! Click the link to contact us!",
               href="https://drive.google.com/drive/folders/1iQzqAF6j5erFxndCa3jmVnO_s4Jvt_1n")

    ])

])

# needed only if running this as a single page app
# if __name__ == '__main__':
#     app.run_server(host='127.0.0.1', debug=True)