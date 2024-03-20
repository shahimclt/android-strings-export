# Strings.xml to excel export script by Mohammed Shahim
# Steps to use:
#     1. Have python installed
#     2. install dependencies: `pip3 install -r .\py_requirements.txt`
#     3. run the script: `python string_export.py`
#     4. Enjoy

# import csv
import os
import xml.etree.ElementTree as ET
import pandas as pd

directory = './app/src/main/res'

string_map = {}

folderNames = []

for root, _, files in os.walk(directory):
    for filename in files:
        if filename == "strings.xml":
            filepath = os.path.join(root, filename)
            folderName = os.path.basename(os.path.dirname(filepath))
            folderNames.append(folderName)
            # Load and parse the strings.xml
            tree = ET.parse(filepath, parser=ET.XMLParser(encoding="UTF-8"))
            root = tree.getroot()
            for string in root.findall("string"):
                # Skip strings marked with translatable="false"
                if string.attrib.get('translatable', 'true') == 'false':
                    continue
                key = string.attrib['name']
                text = string.text
                if key and text:
                    dict = string_map.get(key,{})
                    dict[folderName] = text
                    string_map[key] = dict

header = ["Name"]
for fName in folderNames:
    header.append(fName)

df = pd.DataFrame(columns=header)

rows = []

for key, value in string_map.items():
    value["Name"] = key
    rows.append(value)

df = pd.concat([df, pd.DataFrame(rows)], ignore_index=True)

output_file = "strings.xlsx"
df.to_excel(output_file, index=False)

# Open a CSV file for writing
# with open('strings.csv', 'w', newline='', encoding='UTF-8') as csv_file:
#     # writer = csv.writer(csv_file)
#     # writer.writerow(header)  # Write each row to the CSV
#     for key, value in string_map.items():
#         row = [key]
#         for fName in folderNames:
#             row.append(value.get(fName,""))
#         writer.writerow(row)  # Write the header row


print('Conversion completed. Skipped non-translatable strings. Check strings.csv for the output.')