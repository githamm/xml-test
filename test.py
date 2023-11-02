import csv
import json

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []

    #reading csv (encoding is important)
    with open(csvFilePath, encoding='utf-8') as csvf:
        #csv library function
        csvReader = csv.DictReader(csvf)

        #convert each csv row into python dictionary
        for column in csvReader:
            #add this python dictionary to json array
            jsonArray.append(column)

    #convertion
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)

csvFilePath='election_results_2021.csv'
jsonFilePath='output_2021.json'
csv_to_json(csvFilePath, jsonFilePath)