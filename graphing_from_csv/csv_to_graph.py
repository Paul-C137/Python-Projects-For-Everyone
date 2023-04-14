#!usr/bin/python3
'''lackhack.tech | Paul Lack
   Using matplotlib to plot weather data from a csv file.
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
    # open csv file
    with open("weather_data_bellingham_2023_1.csv", "r") as rain_file:
        rain_data = csv.reader(rain_file, delimiter=",")
        for row in rain_data:
            rain_amount = (row[4])
            date_data = (row[2])
            if rain_amount == '':
                rain_amount = '0'
            rain.append(float(rain_amount))
            date.append(date_data)
    return rain, date

def main():
    rain, date = parse_csv()
    N = len(rain)
    ind = np.arange(N)
    width = .5
    p1 = plt.bar(ind, rain, width, color='green')
    plt.ylabel("Rain (inches)")
    plt.title("Jan 2023 Rainfall")
    plt.xticks(ind, date, rotation=45, fontsize='xx-small', ha='right')
    plt.yticks(np.arange(0, 1, .1))
    plt.legend(["Rain"])
    # SAVE the graph locally
    plt.savefig("Rainfall_2023_NWWashington.png")


if __name__ == "__main__":
    main()
