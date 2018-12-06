import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np


def main():
    crash_data_2017 = pd.DataFrame()
    crash_data_2017 = pd.read_csv("Cleaned_2017.csv", index_col=False)
    crash_data_2018 = pd.DataFrame()
    crash_data_2018 = pd.read_csv("Cleaned_2018.csv", index_col=False)
    monday_crash_count = [0] * 24
    tuesday_crash_count = [0] * 24
    wednesday_crash_count = [0] * 24
    thursday_crash_count = [0] * 24
    friday_crash_count = [0] * 24
    saturday_crash_count = [0] * 24
    sunday_crash_count = [0] * 24


    july_monday_crash_count = [0] * 24
    july_tuesday_crash_count = [0] * 24
    july_wednesday_crash_count = [0] * 24
    july_thursday_crash_count = [0] * 24
    july_friday_crash_count = [0] * 24
    july_saturday_crash_count = [0] * 24
    july_sunday_crash_count = [0] * 24

    days_times = list()
    #create x labels
    for day in range(0,7):
        for x in range(0, 24):
            # hours = x // 2
            # minutes = x % 2
            # if (minutes == 1):
            #     minutes = "30"
            # else:
            minutes = "00"
            weekday =""
            if(day ==0):
                weekday = "M"
            elif(day==1):
                weekday = "T"
            elif(day==2):
                weekday = "W"
            elif(day==3):
                weekday = "TH"
            elif(day==4):
                weekday = "F"
            elif(day==5):
                weekday = "SAT"
            elif(day==6):
                weekday = "SUN"
            # label = weekday + " " + str(hours) + ":" + minutes
            # label = str(hours) + ":" + minutes
            label = weekday + " " + str(x) + ":" + minutes
            days_times.append(label)

    for index, row in crash_data_2017.iterrows():
        data = row['DATE']
        split_data = data.split("/")
        #find index in the list of crash times that needs to be incremented
        time_of_crash = row['TIME']
        split_time = time_of_crash.split(":")
        hours = int(split_time[0])
        if(split_data[0] == '06'):
            if((int(split_data[1])-1) == 0%7):
                #thursday
                thursday_crash_count[hours] = thursday_crash_count[hours] +1
            elif((int(split_data[1])-1) == 1%7):
                #friday
                friday_crash_count[hours] = friday_crash_count[hours] +1
            elif((int(split_data[1])-1) == 2%7):
                #Saturday
                saturday_crash_count[hours] = saturday_crash_count[hours] +1
            elif((int(split_data[1])-1) == 3%7):
                #Sunday
                sunday_crash_count[hours] = sunday_crash_count[hours] +1
            elif((int(split_data[1])-1) == 4%7):
                #Monday
                monday_crash_count[hours] = monday_crash_count[hours] +1
            elif((int(split_data[1])-1) == 5%7):
                #tuesday
                tuesday_crash_count[hours] = tuesday_crash_count[hours] + 1
            elif((int(split_data[1])-1) == 6%7):
                #Wednesday
                wednesday_crash_count[hours] = wednesday_crash_count[hours] + 1
        elif(split_data[0] == '07'):
            if((int(split_data[1])-1) == 0%7):
                #Saturday
                july_saturday_crash_count[hours] = july_saturday_crash_count[hours] + 1
            elif((int(split_data[1])-1) == 1%7):
                #Sunday
                july_sunday_crash_count[hours] = july_sunday_crash_count[hours] +1
            elif((int(split_data[1])-1) == 2%7):
                #Monday
                july_monday_crash_count[hours] = july_monday_crash_count[hours] +1
            elif((int(split_data[1])-1) == 3%7):
                #Tuesday
                july_tuesday_crash_count[hours] = july_tuesday_crash_count[hours] + 1
            elif((int(split_data[1])-1) == 4%7):
                #Wednesday
                july_wednesday_crash_count[hours] = july_wednesday_crash_count[hours] + 1
            elif((int(split_data[1])-1) == 5%7):
                #Thursday
                july_thursday_crash_count[hours] = july_thursday_crash_count[hours] +1
            elif((int(split_data[1])-1) == 6%7):
                #Friday
                july_friday_crash_count[hours] = july_friday_crash_count[hours] +1



    june_graph_data = list()
    july_graph_data = list()
    for x in range(0, len(monday_crash_count)):
        june_graph_data.append(monday_crash_count[x])
    for x in range(0, len(tuesday_crash_count)):
        june_graph_data.append(tuesday_crash_count[x])
    for x in range(0, len(wednesday_crash_count)):
        june_graph_data.append(wednesday_crash_count[x])
    for x in range(0, len(thursday_crash_count)):
        june_graph_data.append(thursday_crash_count[x])
    for x in range(0, len(friday_crash_count)):
        june_graph_data.append(friday_crash_count[x])
    for x in range(0, len(saturday_crash_count)):
        june_graph_data.append(saturday_crash_count[x])
    for x in range(0, len(sunday_crash_count)):
        june_graph_data.append(sunday_crash_count[x])

    for x in range(0, len(july_monday_crash_count)):
        july_graph_data.append(july_monday_crash_count[x])
    for x in range(0, len(july_tuesday_crash_count)):
        july_graph_data.append(july_tuesday_crash_count[x])
    for x in range(0, len(july_wednesday_crash_count)):
        july_graph_data.append(july_wednesday_crash_count[x])
    for x in range(0, len(july_thursday_crash_count)):
        july_graph_data.append(july_thursday_crash_count[x])
    for x in range(0, len(july_friday_crash_count)):
        july_graph_data.append(july_friday_crash_count[x])
    for x in range(0, len(july_saturday_crash_count)):
        july_graph_data.append(july_saturday_crash_count[x])
    for x in range(0, len(july_sunday_crash_count)):
        july_graph_data.append(july_sunday_crash_count[x])


   # plt.bar(days_times, graph_data, alpha=1.0)
    # plt.xlabel("Time of Day")
    # plt.xticks(days_times, rotation='vertical')
    # plt.ylabel("Number of Crashes")
    # plt.title("Times of Car Crashes")
    # plt.show()
    plt.figure(1)
    plt.bar(days_times[0:72],june_graph_data[0:72], alpha=0.2)
    plt.xlabel("Time of the Day")
    plt.ylabel("Number of Crashes")
    plt.xticks(days_times[0:72], rotation='vertical')
    plt.tick_params(axis = 'both', which = 'major', labelsize=6)
    plt.title("Times of Car Crashes Monday through Wednesday in June of 2017")
    plt.figure(2)
    plt.bar(days_times[72:], june_graph_data[72:], alpha = 0.2)
    plt.xlabel("Time of the Day")
    plt.ylabel("Number of Crashes")
    plt.xticks(days_times[72:], rotation='vertical')
    plt.tick_params(axis = 'both', which = 'major', labelsize=6)
    plt.title("Times of Car Crashes Thursday through Sunday in June of 2017")
    plt.figure(3)
    plt.bar(days_times[0:72], july_graph_data[0:72], alpha=0.2)
    plt.xlabel("Time of the Day")
    plt.ylabel("Number of Crashes")
    plt.xticks(days_times[0:72], rotation='vertical')
    plt.tick_params(axis='both', which='major', labelsize=6)
    plt.title("Times of Car Crashes Monday through Wednesday in July of 2017")
    plt.figure(4)
    plt.bar(days_times[72:], july_graph_data[72:], alpha=0.2)
    plt.xlabel("Time of the Day")
    plt.ylabel("Number of Crashes")
    plt.xticks(days_times[72:], rotation='vertical')
    plt.tick_params(axis='both', which='major', labelsize=6)
    plt.title("Times of Car Crashes Thursday through Sunday in July of 2017")

    #------------------------------2018 Chart Creation

    june_monday_crash_count_2018 = [0] * 24
    june_tuesday_crash_count_2018 = [0] * 24
    june_wednesday_crash_count_2018 = [0] * 24
    june_thursday_crash_count_2018 = [0] * 24
    june_friday_crash_count_2018 = [0] * 24
    june_saturday_crash_count_2018 = [0] * 24
    june_sunday_crash_count_2018 = [0] * 24

    july_monday_crash_count_2018 = [0] * 24
    july_tuesday_crash_count_2018 = [0] * 24
    july_wednesday_crash_count_2018 = [0] * 24
    july_thursday_crash_count_2018 = [0] * 24
    july_friday_crash_count_2018 = [0] * 24
    july_saturday_crash_count_2018 = [0] * 24
    july_sunday_crash_count_2018 = [0] * 24
    for index, row in crash_data_2018.iterrows():
        data = row['DATE']
        split_date = data.split("/")
        # find index in the list of crash times that needs to be incremented
        time_of_crash = row['TIME']
        split_time = time_of_crash.split(":")
        hours = int(split_time[0])
        if(split_date[0]=='06'):
            #june
            if((int(split_date[1])-1) == 0%7):
                #friday
                june_friday_crash_count_2018[hours] = june_friday_crash_count_2018[hours] +1
            elif((int(split_date[1])-1) == 1%7):
                #saturday
                june_saturday_crash_count_2018[hours] = june_saturday_crash_count_2018[hours] + 1
            elif((int(split_date[1])-1) == 1%7):
                #Sunday
                june_sunday_crash_count_2018[hours] = june_sunday_crash_count_2018[hours] + 1
            elif((int(split_date[1])-1) == 2%7):
                #Monday
                june_monday_crash_count_2018[hours] = june_monday_crash_count_2018[hours] +1
            elif((int(split_date[1])-1) == 3%7):
                #Tuesday
                june_tuesday_crash_count_2018[hours] = june_tuesday_crash_count_2018[hours] + 1
            elif((int(split_date[1])-1)==4%7):
                #Wednesday
                june_wednesday_crash_count_2018[hours] = june_wednesday_crash_count_2018[hours] + 1
            elif((int(split_date[1])-1) == 5%7):
                #Thursday
                june_thursday_crash_count_2018[hours] = june_thursday_crash_count_2018[hours] + 1
            elif((int(split_date[1]) -1) == 6%7):
                #friday
                june_friday_crash_count_2018[hours] = june_friday_crash_count_2018[hours] +1
        elif(split_date[0] == '07'):
            if((int(split_date[1])-1) == 0%7):
                #Sunday
                july_sunday_crash_count_2018[hours] = july_sunday_crash_count_2018[hours] +1
            elif((int(split_date[1])-1)==1%7):
                #Monday
                july_monday_crash_count_2018[hours] = july_monday_crash_count_2018[hours] +1
            elif((int(split_date[1])-1) == 2%7):
                #tuesday
                july_tuesday_crash_count_2018[hours] = july_tuesday_crash_count_2018[hours] +1
            elif((int(split_date[1])-1)==3%7):
                #wednesday
                july_wednesday_crash_count_2018[hours] = july_wednesday_crash_count_2018[hours] +1
            elif((int(split_date[1])-1)==4%7):
                #thursday
                july_thursday_crash_count_2018[hours] = july_thursday_crash_count_2018[hours] +1
            elif((int(split_date[1])-1)==5%7):
                #friday
                july_friday_crash_count_2018[hours] = july_friday_crash_count_2018[hours] +1
            elif((int(split_date[1])-1) == 6%7):
                #saturday
                july_saturday_crash_count_2018[hours] = july_saturday_crash_count_2018[hours] +1


    june_graph_data_2018 =list()
    june_graph_data_2018.extend(june_monday_crash_count_2018)
    june_graph_data_2018.extend(june_tuesday_crash_count_2018)
    june_graph_data_2018.extend(june_wednesday_crash_count_2018)
    june_graph_data_2018.extend(june_thursday_crash_count_2018)
    june_graph_data_2018.extend(june_friday_crash_count_2018)
    june_graph_data_2018.extend(june_saturday_crash_count_2018)
    june_graph_data_2018.extend(june_sunday_crash_count_2018)
    july_graph_data_2018 = list()
    july_graph_data_2018.extend(july_monday_crash_count_2018)
    july_graph_data_2018.extend(july_tuesday_crash_count_2018)
    july_graph_data_2018.extend(july_wednesday_crash_count_2018)
    july_graph_data_2018.extend(july_thursday_crash_count_2018)
    july_graph_data_2018.extend(july_friday_crash_count_2018)
    july_graph_data_2018.extend(july_saturday_crash_count_2018)
    july_graph_data_2018.extend(july_sunday_crash_count_2018)
#---graph data---------
    plt.figure(5)
    plt.bar(days_times[0:72], june_graph_data_2018[0:72], alpha=0.2)
    plt.xlabel("Time of the Day")
    plt.ylabel("Number of Crashes")
    plt.xticks(days_times[0:72], rotation='vertical')
    plt.tick_params(axis='both', which='major', labelsize=6)
    plt.title("Times of Car Crashes Monday through Wednesday in June of 2018")
    plt.figure(6)
    plt.bar(days_times[72:], june_graph_data_2018[72:], alpha=0.2)
    plt.xlabel("Time of the Day")
    plt.ylabel("Number of Crashes")
    plt.xticks(days_times[72:], rotation='vertical')
    plt.tick_params(axis='both', which='major', labelsize=6)
    plt.title("Times of Car Crashes Thursday through Sunday in June of 2018")
    plt.figure(7)
    plt.bar(days_times[0:72], july_graph_data_2018[0:72], alpha=0.2)
    plt.xlabel("Time of the Day")
    plt.ylabel("Number of Crashes")
    plt.xticks(days_times[0:72], rotation='vertical')
    plt.tick_params(axis='both', which='major', labelsize=6)
    plt.title("Times of Car Crashes Monday through Wednesday in July of 2018")
    plt.figure(8)
    plt.bar(days_times[72:], july_graph_data_2018[72:], alpha=0.2)
    plt.xlabel("Time of the Day")
    plt.ylabel("Number of Crashes")
    plt.xticks(days_times[72:], rotation='vertical')
    plt.tick_params(axis='both', which='major', labelsize=6)
    plt.title("Times of Car Crashes Monday through Wednesday in June of 2018")
    plt.show()
main()