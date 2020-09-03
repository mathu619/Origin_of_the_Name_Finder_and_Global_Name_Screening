# Import necessary libraries
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas as pd

# Import test data to be processed
data_raw = pd.read_csv('sample.csv')

# Function to find the origin of the name supplied by the df
def name_orgin_finder(name):
    return(process.extract(name, names_cleaned_dict_final, limit=1)[0][2].split('_')[0])

# Initiate a list for appending origin matches
origin = []

# Loop to find the origin of each name and append it to the initiated list file
for key, value in data_raw['column_c'].iteritems():
    origin.append(name_orgin_finder(data_raw.loc[key, 'column_c']))
print(origin)    

# Merge the results to the original df
data_raw['ORIGIN'] = origin

# Export the table to excel file
data_raw.to_excel('name_origins.xlsx', index=False)
