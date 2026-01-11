import dash
from dash import dcc, html
import plotly.graph_objs as go
import pandas as pd 
import os

data_path = os.path.join(os.path.dirname(__file__), 'pink_morsels_sales.csv')
df = pd.read_csv(data_path)

df['date'] = pd.to_datetime(df['Date'])
df = df.sort_values('date')

df_grouped = df.groupby('Date')['Sales'].sum().reset_index()

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(
        'pink Morsels Sales Vosualizer',
        style={
            'textAlign':'center',
            'color': '#FF1493',
            'marginTop': '20px',
            'marginBottom': '30px',
            'fontFamily': 'Arial, sans-serif'

        }
    ),
    html.H3(
        'Sales Analyisis: Before vs After Price Increase (Jan 15, 2021)',
        style={
            'textAlign': 'center',
            'color': '#555',
            'marginBottom': '40px',
            'fontFamily': 'Arial, sans-serif'
        }
    ),
    dcc.Graph(
        id='sales-chart',
        figure={
            'data': [
                go.Scatter(
                    x=df_grouped['Date'],
                    y=df_grouped['Sales'],
                    mode='lines',
                    name='Total Sales',
                    line=dict(color="#C90707",width=2)
                    
                )
            ],
            'layout': go.Layout(
                title='Pink Morsels Daily Sales Over time',
                xaxis={'title': 'date'},
                yaxis={'title': 'Sales($)'},
                hovermode='closest',
                height=600,
                shapes=[
                    dict(
                        type='line',
                        x0='2021-01-15',
                        x1='2021-01-15',
                        y0=0,
                        y1=1,
                        yref='paper',
                        line=dict(
                            color='red',
                            width=2,
                            dash='dash',
                        )
                    )
                ],
                annotations = [
                    dict(
                        x='2021-01-155',
                        y=1,
                        yref='paper',
                        text='Price Increase',
                        showarrow=True,
                        arrowhead=2,
                        arrowcolor='red',
                        ax=0,
                        ay=-40,
                    )
                ]
            )
        
        }
    )
])

if __name__ == '__main__':
    app.run(debug=True, port=8050)


