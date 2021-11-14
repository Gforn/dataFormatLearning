import pandas as pd
from dicttoxml import dicttoxml
import json
filename = "shortcuts.csv"

# reading data from csv by pandas
data = pd.read_csv(filename)

# converting the dataframe to a dictionary
data_dict = data.to_dict(orient="records")
with open('csv2json.json', "w+") as json_file:
    json.dump(data_dict, json_file, indent=4)

# converting the dataframe to XML
xml_data = dicttoxml(data_dict).decode()
with open("csv2xml.xml", "w+") as xml_file:
    xml_file.write(xml_data)
