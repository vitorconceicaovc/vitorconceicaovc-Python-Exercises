import pandas as pd

excel_file = 'PythonAndExelFile/ExelFile.xlsx'
panilha = pd.read_excel(excel_file)

numbers_range = int(input("Numbers range: "))

for index in range(1, numbers_range + 1):
    panilha[f'Number_{index}'] = index

# Save to a new Excel file
output_excel_file = 'PythonAndExelFile/UpdatedFile.xlsx'
panilha.to_excel(output_excel_file, index=False)

print(panilha.head())
