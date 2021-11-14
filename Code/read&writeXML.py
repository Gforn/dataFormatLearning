import xml.etree.ElementTree as ET
import xmltodict
# from dicttoxml import dicttoxml
import dicttoxml
import json

tree = ET.parse('csv2xml.xml')
xml_data = tree.getroot()
xmlstr = ET.tostring(xml_data, encoding='utf8', method='xml')
data_dict = dict(xmltodict.parse(xmlstr))

# write to xml
# xml_data = dicttoxml(data_dict).decode()
xml_data = dicttoxml.dicttoxml(data_dict).decode()
with open("shortcutsByXml.xml", "w+") as xml_file:
    xml_file.write(xml_data)

# xml to json
with open('xml2Json.json', 'w+') as json_file:
    json.dump(data_dict, json_file, indent=4, sort_keys=True)
