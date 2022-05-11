import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Logout", href='/logout')),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("List of KPIs", header=True),
                dbc.DropdownMenuItem("KPI 1", href="/kpi1/"),
                dbc.DropdownMenuItem("KPI 2", href="/kpi2/"),
                dbc.DropdownMenuItem("KPI 3", href="/kpi3/"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="IBERIA",
    brand_href="/",
    color="primary",
    dark=True,
    fluid=True,
    links_left=True,
)

