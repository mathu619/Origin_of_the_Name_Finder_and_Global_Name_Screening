import pandas as pd
import itertools as it
import numpy as np

names_cleaned = names.copy(deep=True)
#names_cleaned.to_excel('C:/Users/Mathu/Desktop/GNS Automation/names_cleaned.xlsx', index=True)

# Remove crawler tags
names_cleaned = names_cleaned[~names_cleaned.Name.str.contains('googletag')]

# Remove rows with has 'Origin' as 'Uknown'
names_cleaned = names_cleaned[~names_cleaned.Origin.str.contains('Unknown')]

# Remove rows for which 'Origin' is empty
names_cleaned = names_cleaned[~names_cleaned['Origin'].isnull()]

# Remove rows for which 'Name' is empty
names_cleaned = names_cleaned[~names_cleaned['Name'].isnull()]

# Slice only columns 'Name' and 'Origin'
names_cleaned = names_cleaned.loc[:,['Name','Origin','Similar']]

# To split the similar names in 'Similar' column and add that to the main data column
# Slice only rows having non NA values in 'Similar' columns
names_cleaned_only_non_null = names_cleaned[~names_cleaned['Similar'].isnull()]

# Initiate a dataframe to append the split names data into
final_names_split_df = pd.DataFrame()
#print(final_names_split_df)

# Function to split the names in 'Similar' column and add them to the intermediate dataframe
def name_splitter(names_to_be_split, origin, split_by):
    # Create a list of lists containing split names of 'Similar' column and 'Origin' column
    split_names = list([names_to_be_split.split(split_by), origin])
    #print(split_names)

    # Create a list of list from the previous list to format it in ways to create a dataframe 
    split_names_formated = list([split_names[0],
                      list(it.repeat(split_names[1],len(split_names[0]))),
                      it.repeat(np.nan,len(split_names[0]))])
    #print(split_names)

    # Create a dataframe from the previous list
    df = pd.DataFrame(list(zip(split_names_formated[0],
                           split_names_formated[1],
                           split_names_formated[2])),
                  columns=list(names_cleaned_only_non_null.columns))
    #print(df)
    global final_names_split_df
    final_names_split_df = final_names_split_df.append(df, ignore_index = True)





# Loop to split all rows of 'Similar' column and to add them to the intermediate dataframe 
# by using 'names_splitter' funciton  



# Loop to split all rows of 'Name' column which has multiple names in it 
# and to add them to the intermediate dataframe 
# by using 'names_splitter' funciton  


# Append the intermediate dataframe to the main dataframe
names_cleaned = names_cleaned.append(final_names_split_df)

# Remove 'Similar' column
names_cleaned = names_cleaned.loc[:,['Name','Origin']]

# Reduce origin names by clubbing similar ones

# Remove duplicate names

# Remove symbols from dataset

# Remove accent marks from names




print(final_names_split_df)

# Set index to be used as keys for the dict to be created
names_cleaned = names_cleaned.set_index(names_cleaned['Origin']+'_'+names_cleaned['Name'])
names_cleaned = names_cleaned[['Name']]

# Transpose and Convert dataframe to dictionary for using with fuzzywuzzy
names_cleaned_dict_final = names_cleaned.transpose().to_dict('list')

print(names_cleaned_dict_final)
