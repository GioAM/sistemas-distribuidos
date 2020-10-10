import csv
stock = {}
with open('../estoque/estoque_1.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        stock[row['product_id']] = row['stock']
print(stock['prod1'])