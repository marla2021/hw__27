# importing the required libraries
import csv
import json


# defining the function to convert CSV file to JSON file
def convjson(csvFilename, jsonFilename):
    # creating a dictionary
    mydata = {}

    # reading the data from CSV file
    with open(csvFilename, encoding='utf-8') as csvfile:
        csvRead = csv.DictReader(csvfile)

        # Converting rows into dictionary and adding it to data
        for rows in csvRead:
            mykey = rows['id']
            mydata[mykey] = rows

            # dumping the data
    with open(jsonFilename, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(json.dumps(mydata, indent=4))

    # filenames


csvFilename = r'categories.csv'
jsonFilename = r'json_cat.json'

# Calling the convjson function
convjson(csvFilename, jsonFilename)

csvFilename = r'ads.csv'
jsonFilename = r'json_ad.json'

# Calling the convjson function
convjson(csvFilename, jsonFilename)