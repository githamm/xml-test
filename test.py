import xmltodict
import json
xml_file=open("election_data_2021.xml","r")
xml_string=xml_file.read()
python_dict=xmltodict.parse(xml_string)
json_string=json.dumps(python_dict)
print("The JSON string is:")
print(json_string)