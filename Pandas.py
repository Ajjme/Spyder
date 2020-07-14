# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 12:41:15 2020

@author: ajj4p
"""
#big data and flexability
#save data u are using in same directory

import pandas as pd

#loading in as a data frame

df = pd.read_csv('pokemon_data.csv') # only short path because both files in same spot
print(df.head(3)) #spits out just the top tail also works number not needed 

#pd.read_excel if .xlsx file
#pd.read_csv('pokemon_data.txt, delimiter = '\t') can change based on what is seperating you data

df.columns
#print(df[['Name', 'Type 1', 'HP']])
#to get specific rows iloc function
print(df.iloc[0:4])

#specifitic spot (row, column)
print(df.iloc[2,1])

#Loop!!!
#for index, row in df.iterrows():
    #print(index, row['Name'])
    
# looking things up by a quality
#SUPER POWERFUL
#print(df.loc[df['Type 1'] =="Fire"])

#type 2 is another vairable in data set Bug is a possible answer
#print(df.loc[df["Type 2"] == "Bug"])

#basic stat stuff
#print(df.describe())

#?????????????
#print(df.sort_values('Type 1', ascending = False)


####manipulating data

#creating new column
df['BestAttack'] = df['Attack'] + df['Speed'] + df['Sp. Atk']
print(df.head(5))
#check that it is the right number

#Drop columns

df.drop(columns = ["BestAttack"])
print(df.head(5))

#end paramerter in list is exclusive

#df{{'BestAttack', 'HP', 'Defense'}}







