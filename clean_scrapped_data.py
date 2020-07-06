import pandas as pd

names_cleaned = names.copy(deep=True)
names_cleaned.to_excel('C:/Users/Mathu/Desktop/GNS Automation/names_cleaned.xlsx', index=True)

print(names_cleaned)
names.shape
names_cleaned.shape

# Remove crawler tags
names_cleaned = names_cleaned[~names_cleaned.Name.str.contains('googletag')]

# Remove rows with has Origin as 'Uknown'
names_cleaned = names_cleaned[~names_cleaned.Origin.str.contains('Unknown')]

# Slice only columns 'Name' and 'Origin'
names_cleaned = names_cleaned.loc[:,['Name','Origin','Similar']]

