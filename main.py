import pandas as pd

read_file = pd.read_excel (r'Path where the Excel file is stored\File name.xlsx')
read_file.to_csv (r'Path to store the CSV file\File name.csv', index = None, header=True)