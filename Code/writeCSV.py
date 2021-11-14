import csv
import pandas as pd
# reading data from excel
data = pd.read_excel('shortcuts.xlsx')

# writing to csv file by pandas tool
data.to_csv("shortcutsByPandas.csv", index=False, header=True)

# writing to csv file by csv tool
filename = "shortcutsByCsv.csv"
with open(filename, 'w+', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(data.head())
    csvwriter.writerows(data.values)
