
import csv
import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px



def lineChart():

    df = pd.read_csv('soul_foods_sales.csv')

    fig = px.line(df, x="date", y="sales")

    app.layout = html.Div(children=[
    html.H1(children='Pink morcel sales'),

    dcc.Graph(
        id='pinkMorcel-graph',
        figure=fig
    )
])


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
