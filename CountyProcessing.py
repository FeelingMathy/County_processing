#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import pandas library
import pandas as pd
import numpy as np


#this section just creates column data and row labels

# Race/Ethnicity column
RaceEth = ['Total White',
           'White Hispanic',
           'White Non-Hispanic',
           'White Unknown',
           'Total Black',
           'Black Hispanic',
           'Black Non-Hispanic',
           'Black Unknown',
           'Total Other',
           'Other Hispanic',
           'Other Non-Hispanic',
           'Other Unknown',
           'Total Unknown',
           'Unknown Hispanic',
           'Unknown Non-Hispanic',
           'Unknown Unknown',
           'Total All'
          ]

# County names for forming column names
countyNames = ['Alachua',
'Baker',
'Bay',
'Bradford',
'Brevard',
'Broward',
'Calhoun',
'Charlotte',
'Citrus',
'Clay',
'Collier',
'Columbia',
'DeSoto',
'Dixie',
'Duval',
'Escambia',
'Flagler',
'Franklin',
'Gadsden',
'Gilchrist',
'Glades',
'Gulf',
'Hamilton',
'Hardee',
'Hendry',
'Hernando',
'Highlands',
'Hillsborough',
'Holmes',
'Indian River',
'Jackson',
'Jefferson',
'Lafayette',
'Lake',
'Lee',
'Leon',
'Levy',
'Liberty',
'Madison',
'Manatee',
'Marion',
'Martin',
'Miami-Dade',
'Monroe',
'Nassau',
'Okaloosa',
'Okeechobee',
'Orange',
'Osceola',
'Palm Beach',
'Pasco',
'Pinellas',
'Polk',
'Putnam',
'Santa Rosa',
'Sarasota',
'Seminole',
'St. Johns',
'St. Lucie',
'Sumter',
'Suwannee',
'Taylor',
'Union',
'Volusia',
'Wakulla',
'Walton',
'Washington']

allCounties = []

for i in countyNames:
    name = i + " Cases"
    allCounties.append(name)
    name = i + " Hospitalizations"
    allCounties.append(name)
    name = i + " Deaths"
    allCounties.append(name)

#Creates empty data frame using these as columns
final = pd.DataFrame(columns=allCounties, index=RaceEth)


# In[2]:


#Reads .csv
CountyData = pd.read_csv('county_reports_20200425.csv',delimiter=',',header=0, encoding='ascii',engine='python')

#drops unneeded columns
CountyData.drop(['Race, ethnicity','Unnamed: 0','Cases%','Hospitalizations%','Empty','Deaths%'], axis=1, inplace = True)

#renames remaining 3 columns to covid status
CountyData.columns = ['Cases','Hospitalizations','Deaths']

#allows removal of decimal from deaths
CountyData.Deaths = CountyData.Deaths.astype(float)
pd.options.display.float_format = '{:,.0f}'.format


# In[3]:


#function for carving up main DF into mini DF
def create_df( row, col ):
    df = CountyData.iloc[row:row+17,col].copy()
    df.index = RaceEth
    return df

#carves up main DF into mini DF, then collates them back into the main DF
col = 0
row = 0
for many in range(67): #YES I REALIZE THIS IS BAD don't @ me
    for i in range(0,18):
        for j in range(3):
            final.iloc[0:17,j+row] = create_df(col, j)
    col += 18        
    row += 3

#hook OUTPUT code in here maybe?





# In[ ]:





# In[ ]:




