# Strings.xml to excel export script by Mohammed Shahim
# Steps to use:
#     1. Have python installed
#     2. install dependencies: `pip3 install -r .\py_requirements.txt`
#     3. run the script: `python string_export.py`
#     4. Enjoy

# import csv
import os
import pandas as pd
from lxml import etree

# Load the Excel file
df = pd.read_excel("strings.xlsx")

# Iterate over each column in the row
for column in df.columns:
    if column != "Name" and column != "values":

        # Create the directory for the XML file if it doesn't exist
        directory = f"./app/src/main/res/{column}"
        os.makedirs(directory, exist_ok=True)

        filepath = os.path.join(directory, "strings.xml")
        srcTree = etree.parse(filepath)
        root = srcTree.getroot()
        # for string in :

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
            string_element = root.find("./string[@name='%s']" % string_name)
            if string_element is not None:
                string_element.text = string_value
            else:
                # Create an XML element for the string
                string_element = etree.Element("string", {"name": string_name})
                string_element.text = string_value
                root.append(string_element)

        srcTree.write(filepath, pretty_print=True, xml_declaration=True, encoding='utf-8')

print('Conversion completed. Skipped non-translatable strings. Check strings.csv for the output.')