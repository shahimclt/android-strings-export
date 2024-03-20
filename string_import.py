# Strings.xml to excel export script by Mohammed Shahim
# Steps to use:
#     1. Have python installed
#     2. install dependencies: `pip3 install -r .\py_requirements.txt`
#     3. run the script: `python string_export.py`
#     4. Enjoy

# import csv
import os
import pandas as pd
import xml.etree.ElementTree as ET
import xml.dom.minidom

# Load the Excel file
df = pd.read_excel("strings.xlsx")

# Iterate over each column in the row
for column in df.columns:
    if column != "Name" and column != "values":

        # Create the root element for the XML file
        root = ET.Element("resources")

        # Iterate over each row in the DataFrame
        for _, row in df.iterrows():
            # Get the string name
            string_name = row["Name"]
            # Get the string value
            string_value = row[column]

            # Skip if the string value is NaN
            if pd.isna(string_value):
                continue

            # Create an XML element for the string
            string_element = ET.Element("string", {"name": string_name})
            string_element.text = string_value
            root.append(string_element)

        # Create an ElementTree object from the root element
        # tree = ET.ElementTree(root)

        # Create a string representation of the XML tree
        xml_string = ET.tostring(root, encoding="UTF-8")

        # Parse the XML string with minidom
        dom = xml.dom.minidom.parseString(xml_string)

        # Pretty-print the XML
        pretty_xml = dom.toprettyxml(indent="  ")

        # Create the directory for the XML file if it doesn't exist
        directory = f"./app/src/main/res/{column}"
        os.makedirs(directory, exist_ok=True)

        # Write the XML file
        with open(f"{directory}/strings.xml", "w", encoding="utf-8") as file:
            file.write(pretty_xml)

print('Conversion completed. Skipped non-translatable strings. Check strings.csv for the output.')