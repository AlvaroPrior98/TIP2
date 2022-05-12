import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Logout", href='http://127.0.0.1:5000/logout')),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("List of KPIs", header=True),
                dbc.DropdownMenuItem("KPI 1", href="http://127.0.0.1:5000/kpi1/"),
                dbc.DropdownMenuItem("KPI 2", href="http://127.0.0.1:5000/kpi2/"),
                dbc.DropdownMenuItem("KPI 3", href="http://127.0.0.1:5000/kpi3/"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="IBERIA",
    brand_href="http://127.0.0.1:5000/",
    color="primary",
    dark=True,
    fluid=True,
    links_left=True,
)

