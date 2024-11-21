# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import os
import pandas

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Choose which format the output file should be:
    print("Choose the output file format. Enter 1 or 2  : [1] csv , [2] xlsx ")
    output_format = input()
    while output_format not in ["1", "2"]:
        print("Please try again select 1 OR 2\nChoose the output file format : [1] csv , [2] xlsx \n")
        output_format = input()

    # open the file with read permissions.
    while True:
        try:
            # Ask the user to input the path to the file.
            print("Please enter the path of the file: ")
            file_path = input()
            input_file1 = open(file_path, 'r')
            # break the loop if file opened successfully.
            break

        except FileNotFoundError:
            print(f"Error: file not found at {file_path}. Please check the file path and try again:")

    # In case we want to use the script with argument instead of creating a dialog with the user and ask for file path.
    # Check how many arguments the user sent
    # argc = len(sys.argv) - 1
    # if argc != 1 :
    #    print("Input file doesn't exist, run the script again with one file name with one of the formats: xlsx/csv. \n goodbye")
    #    exit(0)

    # Check is the file is in the right format
    # input_file1 = sys.argv[1]

    file1_format = "Unsupported format"
    if ".csv" in file_path:
        file1_format = ".csv"
        # Read the CSV file into a dataframe
        dataframe = pandas.read_csv(input_file1)

    elif ".xlsx" in file_path:
        file1_format = ".xlsx"
        # Read the CSV file into a dataframe
        dataframe = pandas.read_excel(input_file1)
    # The file isn't in the right format
    if file1_format == "Unsupported format":
        print("The script supports only xlsx/csv files. Make sure to enter the name of the file you want to filter as"
              " argument, goodbye!")
        exit(0)

    if "1" in output_format:
        output_file = "Indicators_to_append.csv"
    elif "2" in output_format:
        output_file = "Indicators_to_append.xlsx"

    # Create a new Data Frame contains all info we need
    filtered_df = pandas.DataFrame()
    filtered_df['IndicatorType'] = ''
    filtered_df['IndicatorValue'] = ''
    filtered_df['ExpirationTime'] = ''
    filtered_df['Action'] = ''
    filtered_df['Severity'] = ''
    filtered_df['Title'] = ''
    filtered_df['Description'] = ''
    filtered_df['RecommendedActions'] = ''
    filtered_df['RbacGroups'] = ''
    filtered_df['Category'] = ''
    filtered_df['MitreTechniques'] = ''
    filtered_df['GenerateAlert'] = ''

    flag_EOF = False
    for index, row in dataframe.iterrows():
        values = []
        if flag_EOF:
            break
        for column in ['emailIdentifier','sha256','domain','IP','url','md5']:
            flag_EOF = True
            value = row[column]
            if pandas.notna(value) and value != '':
                if column == 'md5':
                    flag_EOF = False
                    continue
                if column == 'IP':
                    value = value.replace('[.]', '.')
                if column == 'domain':
                    value = value.replace('[', '').replace(']', '')
                if column == 'url':
                    value = value.replace('hxxp', 'http').replace('[.]', '.')
                values.append(value)
                if column == 'sha256':
                    filtered_df.at[index, 'Action'] = 'BlockAndRemediate'
                    filtered_df.at[index, 'IndicatorType'] = 'FileSha256'
                    flag_EOF = False
                    break
                else:
                    filtered_df.at[index, 'Action'] = 'Block'
                    if column == 'emailIdentifier':
                        filtered_df.at[index, 'IndicatorType'] = 'Email'
                        flag_EOF = False
                        break
                    elif column == 'domain':
                        filtered_df.at[index, 'IndicatorType'] = 'DomainName'
                        flag_EOF = False
                        break
                    elif column == 'IP':
                        filtered_df.at[index, 'IndicatorType'] = 'IpAddress'
                        flag_EOF = False
                        break
                    elif column == 'url':
                        filtered_df.at[index, 'IndicatorType'] = 'Url'
                        flag_EOF = False
                        break

        if flag_EOF:
            print("END OF FILE")
            break
        if not values:
            continue
        # Join the collected values with a separator
        filtered_df.at[index, 'IndicatorValue'] = ', '.join(values)
        filtered_df.at[index, 'Title'] = "CertIL ID " + str(int(dataframe.at[index, 'reportId'])) + ' ' \
                                         + dataframe.at[index, 'publishDate']
        filtered_df.at[index, 'Description'] = os.path.basename(file_path)
        filtered_df.at[index, 'Severity'] = 'High'
        filtered_df.at[index, 'Category'] = 'None'
        filtered_df.at[index, 'GenerateAlert'] = 'TRUE'

    if output_format == "1":
        if os.path.exists(output_file):
            # Append to the file if it exists
            filtered_df.to_csv(output_file, mode='a', index=False, header=False)
            print(f"Appended to {output_file}.")
        else:
            # Create a new file if it doesn't exist
            filtered_df.to_csv(output_file, index=False)
            print(f"Created new file: {output_file}.")
    if output_format == "2":
        filtered_df.to_excel(output_file, index=False)
    print("Thanks for using my script - TDanny \nGithub: https://github.com/TDanny/\n ")


