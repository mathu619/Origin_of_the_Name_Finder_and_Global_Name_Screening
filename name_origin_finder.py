# Import necessary libraries
#from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas as pd

# Import raw data
data_raw = pd.read_csv('C:/Users/Mathu/Desktop/GNS Automation/sample.csv')
print(data_raw)

#########################################################################
# Simulation data for testinng
# Dataframe output from beautiful soup scrapping
soup_dict = {'names':["Nguyen", "Tran", "Dang","Phan",'Li','Wei','Fang','madhu','baskar','sundar'],'origin':['vietnamese','vietnamese','vietnamese','vietnamese','chiniese','chiniese','chiniese','indian','indian','indian']}

# Master database of names and its origins
soup_df_uncleaned = pd.DataFrame(soup_dict)
soup_df = soup_df_uncleaned.copy(deep=True)
print(soup_df_uncleaned)
#########################################################################

# Actual processing after beautiful soup output starts
# Set index to be used as keys for the dict to be created
soup_df = soup_df.set_index(soup_df['origin']+'_'+soup_df['names'])
soup_df = soup_df[['names']]

# Transpose and Convert dataframe to dictionary for using with fuzzywuzzy
soup_dict_final = soup_df.transpose().to_dict('list')

# Function to find the origin of the name supplied by the df
def name_orgin_finder(name):
    return(process.extract(name, soup_dict_final, limit=1)[0][2].split('_')[0])

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






