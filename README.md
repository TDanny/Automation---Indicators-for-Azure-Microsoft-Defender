# Automation-Scripts
Automation Scripts I created for the use of IT &amp; Software departments.

# ReadMe
Hey,
IndicatorToCsvXlsx.py is python script which automize the process of updating Azure Microsoft Defender Indicators list.
The National Cyber department often publish a document which includes a list of identifiers/indicators of malicious files/domains/urls/IPs and etc.
Instead of wasting time a new CSV file in the format in which azure cloud Defender works with  - I created a script which will do it for you.
It saves time and all you need to do after running the scripts is to edit by yourself the "RecommendedActions" because its changes between each vulnerability published. 

Note: you must install pandas openpyxl for the script to run, use the command :
pip install pandas openpyxl

pandas is a library used for data manipulation.
openpyxl is used to read and write Excel/csv files with '.xlsx' or '.csv' format.

Documentation for pandas: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html

# Syntax & Arguments:
Just run the python script and follow the instruction.
You will choose the output file format you want - "csv" or "xlsx".
When choosing the path to file remember to choose only xlsx/csv file , otherwise the script won't run and will preform exit.

example - how to run the script:
python IndicatorToCsvXlsx.py

# Return Value:
The output of this python script is a CSV/Excel file which built in specific way and structure in aim to upload/append it to the existing Master indicators list.

It might return a error in case you didn't follow the instruction above.

# LinkedIn: https://www.linkedin.com/in/daniel-tredler-06761b213/
# GitHub: https://github.com/TDanny/

# Danny Tred
