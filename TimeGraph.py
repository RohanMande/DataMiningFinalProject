import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np


def main():
    crash_data = pd.DataFrame
    crash_data = pd.read_csv("Cleaned_Data.csv",index_col=False)
    time_data = [0] * 48
    for index, row in crash_data.iterrows():
        time_of_crash = row['TIME']
        split_time =  time_of_crash.split(":")
        index = (2 * int(split_time[0]))
        if(int(split_time[1])>=30):
            index = index + 1
        time_data[index] = time_data[index] + 1
    times = [0] * 48
    for x in range(0, 48):
        hours = x//2
        minutes = x%2
        if(minutes==1):
            minutes = "30"
        else:
            minutes = "00"
        times[x] = str(hours) + ":" + minutes
    print(times)
    plt.bar(times, time_data, alpha=1.0)
    plt.xlabel("Time of Day")
    plt.xticks(times, rotation='vertical')
    plt.ylabel("Number of Crashes")
    plt.title("Times of Car Crashes")
    plt.show()
main()

