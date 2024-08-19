
import csv

def main():
    print("Generated a new csv file called soul_foods_sales")
    salesData()



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



if __name__== "__main__":
    main()