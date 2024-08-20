
import csv
import pandas as pd
from dash import Dash, html, dcc,Input, Output, callback
import plotly.express as px



def lineChart():

    app.layout = html.Div(
    children=[
        # Header
        html.H1(
            children='Pink Morcel Sales',
            id="header",
            style={
                'textAlign': 'center',
                'color': '#ff69b4',
                'fontFamily': 'Arial, sans-serif',
                'fontWeight': 'bold',
                'fontSize': '36px',
                'marginBottom': '20px',
            }
        ),

        # Radio Items for selecting the region
        html.Div(
            dcc.RadioItems(
                ['general', 'north', 'south', 'east', 'west'],
                'general',
                id='chart-type',
                inline=True,
                style={
                    'textAlign': 'center',
                    'marginBottom': '20px',
                    'fontFamily': 'Arial, sans-serif',
                    'fontSize': '18px',
                    'color': '#555',
                }
            )
        ),

        # Graph
        dcc.Graph(
            id='pinkMorcel-graph',
            style={
                'padding': '20px',
                'backgroundColor': '#f9f9f9',
                'borderRadius': '10px',
                'boxShadow': '0px 0px 10px rgba(0, 0, 0, 0.1)',
            }
        )
    ],
    style={
        'backgroundColor': '#f0f0f0',
        'padding': '40px',
        'fontFamily': 'Arial, sans-serif',
    }
)

@callback(
    Output('pinkMorcel-graph', 'figure'),
    Input('chart-type', 'value'),
)
def update_graph(direction):
    df= pd.read_csv('soul_foods_sales.csv')
    df = df.sort_values(by="date")

    if direction != 'general':
        df= df[df['region']== direction]

    fig = px.line(df, x="date", y="sales")
    return fig

def salesData():

    file_paths = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv"
    ]

    processed_rows = []

    for file_path in file_paths:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                if row['product'].lower() == "pink morsel":
                    price = float(row['price'].replace('$', ''))
                    sales = price * int(row['quantity'])
                    
                    processed_rows.append({
                        'sales': sales,
                        'date': row['date'],
                        'region': row['region']
                    })

    output_file_path = "soul_foods_sales.csv" 

    with open(output_file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['sales', 'date', 'region'])
        writer.writeheader()
        writer.writerows(processed_rows)

app = Dash(__name__)


print("Generated a new csv file called soul_foods_sales")
salesData() #can be commented once generated but still on so its constantly updated
lineChart()


if __name__== "__main__":
    app.run(debug=True)
