from mapreduce import *

def read_db(filename):
    db = []
    with open(filename, 'r') as f:
        for l in f:
            db.append(l)
    f.close()
    return db
            
test_db = read_db("/Users/limfuoen/Library/CloudStorage/OneDrive-SingaporeUniversityofTechnologyandDesign/University stuff/Term 6/50.043 - Database Systems/cohortclass/cc10/ex2/data/price.csv")

# TODO: FIXME
# the result should contain a list of suppliers, 
# with the average sale price for all items by this supplier.

suppliers = []
supplier_item = {}
item_price = {}

def split_record(record):
    temp = record.split(',')
    product = temp[0]
    supplier = temp[1]
    price = temp[-1].replace('\n', '')
    return product, supplier, price

for record in test_db:
    product, supplier, price = split_record(record)

    if supplier not in supplier_item.keys():
        supplier_item[supplier] = []

    item_price[product] = float(price)
        
for supplier in suppliers:
    

result = []

# print the results
for supplier,avg_price in result:
    print(supplier, avg_price)