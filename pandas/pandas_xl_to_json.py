#!/usr/bin/python3

'''lackhack.tech | Paul Lack
   Using Pandas to convert an xls file to json
   Put json data into https://jsonformatter.org/json-pretty-print
   to make data pretty.'''
 
import pandas as pd

def main():
    excel_file = 'weather_data_bellingham_2022.xlsx'
    weather = pd.read_excel(excel_file)
    # print the dataframe just so you can see it
    #print(weather)  
    
    # print the first five records in the dataframe
    #print(weather.head())  

    # print the first ten records in the dataframe
    #print(weather.head(10))

    # print the last thirteen records in the dataframe
    #print(weather.tail(13))

    # export data for the first 100 days to json
    weather.head(100).to_json('100_days_of_weather.json')

if __name__ == "__main__":
    main()