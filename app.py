import numpy as np
import pandas as pd
import plotly.graph_objs as go
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

external_stylesheet = [
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh',
        'crossorigin': 'anonymous'
    }
]

patients = pd.read_csv('state_wise_daily.csv')
total = patients.shape[0]
active = patients[patients['Status'] == 'Confirmed'].shape[0]
recovered = patients[patients['Status'] == 'Recovered'].shape[0]
deaths = patients[patients['Status'] == 'Deceased'].shape[0]

options = [
    {'label': 'All', 'value': 'All'},
    {'label': 'Hospitalized', 'value': 'Hospitalized'},
    {'label': 'Recovered', 'value': 'Recovered'},
    {'label': 'Deceased', 'value': 'Deceased'}
]

options1 = [
    {'label': 'All', 'value': 'All'},
    {'label': 'Mask', 'value': 'Mask'},
    {'label': 'Sanitizer', 'value': 'Sanitizer'},
    {'label': 'Oxygen', 'value': 'Oxygen'}
]

options2 = [
    {'label': 'Red Zone', 'value': 'Red Zone'},
    {'label': 'Blue Zone', 'value': 'Blue Zone'},
    {'label': 'Green Zone', 'value': 'Green Zone'},
    {'label': 'Orange Zone', 'value': 'Orange Zone'},
    {'label': 'All', 'value': 'Status'}  # Added 'All' option
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheet)
app.layout = html.Div([
    html.H1("Corona Virus Pandemic", style={'color': '#fff', 'text-align': 'center'}),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Total Cases", className='text-light'),
                    html.H4(total, className='text-light')
                ], className='card-body')
            ], className='card bg-danger')
        ], className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Active Cases", className='text-light'),
                    html.H4(active, className='text-light')
                ], className='card-body')
            ], className='card bg-info')
        ], className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Recovered Cases", className='text-light'),
                    html.H4(recovered, className='text-light')
                ], className='card-body')
            ], className='card bg-warning')
        ], className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Total Deaths", className='text-light'),
                    html.H4(deaths, className='text-light')
                ], className='card-body')
            ], className='card bg-success')
        ], className='col-md-3')
    ], className='row'),
    html.Div([
        html.Div([
            html.Div([
                dcc.Dropdown(id='plot-graph', options=options1, value='All'),
                dcc.Graph(id='graph')
            ], className='card-body')
        ], className='card bg-info col-md-6'),
        html.Div([
            html.Div([
                dcc.Dropdown(id='my_dropdown', options=options2, value='Status', style={"width": "100%"}),
                dcc.Graph(id='the_graph')
            ], className='card-body')
        ], className='card bg-success col-md-6')
    ], className='row mt-3'),
    html.Div([
        html.Div([
            html.Div([
                dcc.Dropdown(id='picker', options=options, value='All'),
                dcc.Graph(id='bar')
            ], className='card-body')
        ], className='card bg-warning col-md-12')
    ], className='row mt-3')
], className='container')

# Callback to update the bar chart
@app.callback(Output('bar', 'figure'), [Input('picker', 'value')])
def update_graph(type):
    if type == 'All':
        return {
            'data': [go.Bar(x=patients['State'], y=patients['Total'])],
            'layout': go.Layout(title="State Total Count", plot_bgcolor='orange')
        }
    if type == "Hospitalized":
        return {
            'data': [go.Bar(x=patients['State'], y=patients['Hospitalized'])],
            'layout': go.Layout(title="State Hospitalized Count", plot_bgcolor='orange')
        }
    if type == "Recovered":
        return {
            'data': [go.Bar(x=patients['State'], y=patients['Recovered'])],
            'layout': go.Layout(title="State Recovered Count", plot_bgcolor='orange')
        }
    if type == "Deceased":
        return {
            'data': [go.Bar(x=patients['State'], y=patients['Deceased'])],
            'layout': go.Layout(title="State Deceased Count", plot_bgcolor='orange')
        }

# Callback to generate line graph
@app.callback(Output('graph', 'figure'), [Input('plot-graph', 'value')])
def generate_graph(type):
    if type == 'All':
        return {
            'data': [go.Scatter(x=patients['Status'], y=patients['Total'], mode='lines')],
            'layout': go.Layout(title="Commodities Total Count", plot_bgcolor='pink')
        }
    if type == 'Mask':
        return {
            'data': [go.Scatter(x=patients['Status'], y=patients['Mask'], mode='lines')],
            'layout': go.Layout(title="Mask Distribution", plot_bgcolor='pink')
        }
    if type == 'Sanitizer':
        return {
            'data': [go.Scatter(x=patients['Status'], y=patients['Sanitizer'], mode='lines')],
            'layout': go.Layout(title="Sanitizer Distribution", plot_bgcolor='pink')
        }
    if type == 'Oxygen':
        return {
            'data': [go.Scatter(x=patients['Status'], y=patients['Oxygen'], mode='lines')],
            'layout': go.Layout(title="Oxygen Supply", plot_bgcolor='pink')
        }

# Callback to generate pie chart
@app.callback(Output('the_graph', 'figure'), [Input('my_dropdown', 'value')])
def generate_pie_chart(my_dropdown):
    if my_dropdown in ['Red Zone', 'Blue Zone', 'Green Zone', 'Orange Zone']:
        filtered_df = patients[patients['Zone'] == my_dropdown]
    else:
        filtered_df = patients
    piechart = px.pie(data_frame=filtered_df, names=my_dropdown, hole=0.3)
    return piechart

if __name__ == '__main__':
    app.run_server(debug=True)
