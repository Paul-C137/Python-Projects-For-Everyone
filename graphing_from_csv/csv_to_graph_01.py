#!usr/bin/python3
'''lackhack.tech | Paul Lack
   Using matplotlib to plot weather data from a csv file.
   This script is based on csv_to_graph.py in the same project
   directory.  This script plots two bars to the graph.
   Data can be obtained from https://www.ncei.noaa.gov for
   free or use the example csv file included in this project.'''


import numpy as np 
import matplotlib
import csv
matplotlib.use('Agg')

import matplotlib.pyplot as plt

def clean_data():
    if rain_amount == '':
        rain_amount = '0'

def parse_csv():
    ''' return a list of precipation amounts pulled from csv file'''
    # create an empty list to hold precip data
    rain = []
    date = []
    snow = []
    # open csv file
    with open("weather_data_bellingham_2023_1.csv", "r") as rain_file:
        rain_data = csv.reader(rain_file, delimiter=",")
        for row in rain_data:
            rain_amount = (row[4])
            date_data = (row[2])
            snow_amount = (row[5])
            if rain_amount == '':
                rain_amount = '0'
            if snow_amount == '':
                snow_amount = '0'
            rain.append(float(rain_amount))
            snow.append(float(snow_amount))
            date.append(date_data)
    return rain, date, snow

def main():
    rain, date, snow = parse_csv()
    N = len(rain)
    ind = np.arange(N)
    width = .5
    p1 = plt.bar(ind, rain, width, color='green')
    p2 = plt.bar(ind, snow, width, color='blue')
    plt.ylabel("Precipitation (inches)")
    plt.title("Jan 2023 Precipitation")
    plt.xticks(ind, date, rotation=45, fontsize='xx-small', ha='right')
    plt.yticks(np.arange(0, 1, .1))
    plt.legend(["Rain", "Snow"])
    # SAVE the graph locally
    plt.savefig("Precipitation_Jan_2023.png")


if __name__ == "__main__":
    main()
