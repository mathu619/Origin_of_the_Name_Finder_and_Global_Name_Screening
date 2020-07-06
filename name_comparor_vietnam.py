# Import necessary libraries
import pandas as pd

# Import data
data_raw = pd.read_csv('C:/Users/Mathu/Desktop/GNS Automation/sample.csv')

# Make a copy if the data for further manipulation
data = data_raw.copy(deep=True)

# Remove symbols and punctuations from the data
data['HNM'] = data['HNM'].str.replace(r'\W','')
data['NMT'] = data['NMT'].str.replace(r'\W','')
data['FIELD_6'] = data['FIELD_6'].str.replace(r'\W','')

# Delete the column TUNABLE if its already present in the table(useful when running the iterator multiple times)
try:
    del data['TUNABLE']
except:
    print('Column \'TUNABLE\' is not present in the table')

# Initiate the empty list 'TUNABLE' to append the results into
TUNABLE = []

# iter over each row of the pandas dataframe and check if HNM, NMT, FIELD_6 are all not equal
for key, value in data.iterrows():
#    print((data.loc[key,'HNM'] != data.loc[key,'NMT']) & (data.loc[key,'FIELD_6'] != data.loc[key,'NMT']))
    TUNABLE.append ((data.loc[key,'HNM'] != data.loc[key,'NMT']) & (data.loc[key,'FIELD_6'] != data.loc[key,'NMT']))
#print(TUNABLE)

# Add the result colun 'TUNABLE' in the table
data_raw['TUNABLE']=TUNABLE
#print(data)

# Export the table to a excel file in disc
data_raw.to_excel('C:/Users/Mathu/Desktop/GNS Automation/final.xlsx', index=False)
