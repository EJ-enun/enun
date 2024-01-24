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
app.title = 'Monumentos Madrid'
# Navbar

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="/assets/cmadrid.jpg", height="30px")),
                        dbc.Col(dbc.NavbarBrand("Comunidad De Madrid", className="ml-2")),
                    ],
                    align="center",
                    
                ),
                href="#",
            ),
            dbc.NavbarToggler(id="navbar-toggler"),
            dbc.Collapse(
                dbc.Nav(
                    [
                        dbc.NavItem(dbc.NavLink("Viva Madrid", href="#")),
                        dbc.DropdownMenu(
                            children=[
                                dbc.DropdownMenuItem("More", header=True),
                                dbc.DropdownMenuItem("Events", href="#"),
                                dbc.DropdownMenuItem("Contact Us", href="#"),
                            ],
                            nav=True,
                            in_navbar=True,
                            label="More",
                        ),
                    ], 
                    className="ml-auto", # Aligns navbar items to the right
                    navbar=True
                ),
                id="navbar-collapse",
                navbar=True,
            ),
        ]
    ),
    color="FF0000",
    dark=True,
)

location = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])
app.layout = dbc.Container(fluid=True, children=[navbar, location])


# Define the layout for the homepage
home_layout = html.Div([
    html.H1('Welcome to the History of Madrid App!'),
    dcc.Link('Go to Madrid History', href='/madrid-history'),
])

# Define the layout for the Madrid History page
madrid_layout = html.Div([
    html.H1('History of Madrid'),
    html.P('The documented history of Madrid dates to the 9th century, even though the area has been inhabited since the Stone Age. The primitive nucleus of Madrid, a walled military outpost in the left bank of the Manzanares, dates back to the second half of the 9th century, during the rule of the Emirate of Córdoba[^1^][5].'),
    dcc.Link('Go back to home', href='/'),
])

# Update the index page
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/madrid-history':
        return madrid_layout
    else:
        return home_layout
@app.callback(
    [Output('some_stuff', 'children'),],
    [Input('stuff', 'value')])

def display_something(value):
    return value

if __name__ == '__main__':
    app.run_server(debug=False)