# android-strings-export
A Python script to automate importing and exporting `strings.xml` files to excel. This will help you handover the strings for translation to non technical users

## Steps to use:
    * Have python installed
    * Copy the files to the root of your project
    * if you need to avoid accidentally commiting the exported XLSX to Git, add this to `.gitignore`: `/*.xlsx`
    * install dependencies: `pip3 install -r .\py_requirements.txt`
    * run the script: `python string_export.py`
    * Enjoy

## Export all strings to XLSX:

> python string_export.py

Find and export all string locales into a single excel file. You can edit this file to then add/review translations

## Hard import:

> python string_import.py

Parses the XLSX file and replaces all strings.xml files except the default .Modify the `if` condition in the code if you need to replace that too.

Note: Hard import completely replaces the files and will lose all formatting/comments

## Soft import:

> python string_import_soft.py

Parses the XLSX file and replaces individial values in all strings.xml files except the default .Modify the `if` condition in the code if you need to replace that too.

Note: This script attempts to replace only the modified translations without disturbing the original files formatting/sorting. New strings will be appended at the end, but removed strings will not be deleted (Scope for future improvement)
