import csv
import pandas as pd
filename = "shortcuts.csv"

# reading data from csv by pandas
data = pd.read_csv(filename)
print('Reading data from csv by pandas:')
print(data)
print('#############################################')

# reading data from csv by csv
fields = []
rows = []
with open(filename, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
print('Reading data from csv by csv:')
for row in rows:
    print(row)
