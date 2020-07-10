# Import necessary libraries
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas as pd

# Import test data to be processed
data_raw = pd.read_csv('C:/Users/Mathu/Desktop/GNS Automation/sample.csv')

# Function to find the origin of the name supplied by the df
def name_orgin_finder(name):
    return(process.extract(name, names_cleaned_dict_final, limit=1)[0][2].split('_')[0])

# Initiate a list for appending origin matches
origin = []

# Loop to find the origin of each name and append it to the initiated list file
for key, value in data_raw['FIELD_6'].iteritems():
    origin.append(name_orgin_finder(data_raw.loc[key, 'FIELD_6']))
print(origin)    

# Merge the results to the original df
data_raw['ORIGIN'] = origin

# Export the table to excel file
data_raw.to_excel('C:/Users/Mathu/Desktop/GNS Automation/name_origins.xlsx', index=False)

#################################
# Test
process.extract(data_raw.iloc[0,2], names_cleaned_dict_final)
process.extractOne('Nguymn thu li chin', names_cleaned_dict_final)
process.extract('Nguyen thu li chin', names_cleaned_dict_final)
process.extract('Nguyen', names_cleaned_dict_final)
process.extract('thu', names_cleaned_dict_final)
process.extract('li', names_cleaned_dict_final)
process.extract('chin', names_cleaned_dict_final)



