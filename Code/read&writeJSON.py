import json
import pandas as pd

# read and write json by pandas
data = pd.read_json('csv2json.json', orient='records')
export = data.to_json('shortcutsByPandas.json', orient='records')

# read and write json by json
with open('csv2json.json') as file:
    data = json.load(file)
with open('shortcutsByJson.json', 'w+') as json_file:
    json.dump(data, json_file, indent=4, sort_keys=True)
