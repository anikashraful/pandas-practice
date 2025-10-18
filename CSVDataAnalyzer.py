# import & read the csv file

import pandas as pd 

df = pd.read_csv('my_data.csv')
print(df.head())

# Basic data overview

print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())

# Missing or duplicate data

print(df.isnull().sum())
df = df.drop_duplicates()


# Column Analysis

print(df['Age'].mean())
print(df['Age'].min())
print(df['Age'].max())

# Filtering and Grouping

adults = df[df['Age'] >=18]
print(adults.groupby('Gender').size())