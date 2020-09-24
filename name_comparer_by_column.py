# Import necessary libraries
import pandas as pd

# Import data
data_raw = pd.read_csv('sample.csv')

# Make a copy if the data for further manipulation
data = data_raw.copy(deep=True)

# Remove symbols and punctuations from the data
data['column_a'] = data['column_a'].str.replace(r'\W','')
data['column_b'] = data['column_b'].str.replace(r'\W','')
data['column_c'] = data['column_c'].str.replace(r'\W','')

# Delete the column RESULT if its already present in the table
# (useful when running the iterator multiple times)
try:
    del data['RESULT']
except:
    print('Column \'RESULT\' is not present in the table')

# Initiate the empty list 'RESULT' to append the results into
RESULT = []

# iter over each row of the pandas dataframe and check if column_a, column_b, column_c are all not equal
for key, value in data.iterrows():
    RESULT.append ((data.loc[key,'column_a'] != data.loc[key,'column_b']) & (data.loc[key,'column_c'] != data.loc[key,'column_b']))

# Add the result colun 'RESULT' in the table
data_raw['RESULT']=RESULT

# Export the table to a excel file in disc
data_raw.to_excel('final.xlsx', index=False)
