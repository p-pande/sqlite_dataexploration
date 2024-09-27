import pandas as pd
import sqlite3

### Create connection to SQLite database
conn = sqlite3.connect('healthcare.db')

### Create a Pandas DataFrame
df = pd.read_csv('https://data.cdc.gov/resource/3yf8-kanr.csv')
df['jurisdiction_of_occurrence'].value_counts()
print (df.columns)

### Save DataFrame to the SQLite database
df.to_sql('weekly_death_counts', conn, if_exists='replace', index=False)

## Queries to verify data

query_1 = 'SELECT * FROM weekly_death_counts'
result_df = pd.read_sql(query_1,conn)

print(result_df)

## Count number of records for certain condition

query_2 = """SELECT jurisdiction_of_occurrence, allcause, naturalcause  
            FROM weekly_death_counts
            WHERE jurisdiction_of_occurrence in ("Florida", "Arizona")"""
            
result_df = pd.read_sql(query_2,conn)
print(result_df)

## Group data by a specific column and calculate a summary statistic

query_3 = """SELECT AVG(allcause)
            FROM weekly_death_counts
            WHERE jurisdiction_of_occurrence in ("Florida")"""
result_df = pd.read_sql(query_3,conn)
print(result_df)


## Sort data based on a numerical or categorical field

query_4 = """SELECT *
            FROM weekly_death_counts
            ORDER BY allcause DESC LIMIT 10"""
result_df = pd.read_sql(query_4,conn)
print(result_df)