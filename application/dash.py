import dash
import dash_auth
import dash_bootstrap_components as dbc
from dash import dcc, html, Output, Input, State, dash_table

app = dash.Dash(__name__,
                meta_tags=[
                    {'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}],
                external_stylesheets=[dbc.themes.QUARTZ])
 
#Setup Style Sheets file.  
#app.css.append_css({"external_url": "/application/static/style.css"})

server = app.server
#App Title.
app.title = 'ENUN BASSEY'
# Navbar

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Page 1", href="#")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Page 2", href="#"),
                dbc.DropdownMenuItem("Page 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="NavbarSimple",
    brand_href="#",
    color="primary",
    dark=True,
)
app.layout = dbc.Container(children=[navbar],style={ "height" : "100vh",'width': "100vh"})

@app.callback(
    [Output('some_stuff', 'children'),],
    [Input('stuff', 'value')])

def display_something(value):
    return value

if __name__ == '__main__':
    app.run_server(debug=False)