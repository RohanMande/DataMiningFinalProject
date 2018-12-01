#This class is takes all of the data from the bronx and creates a KML file showing where there were crashes
import pandas as pd
import sys





def main():
    raw_data = pd.DataFrame()
    raw_data = pd.read_csv("NYPD_Motor_Vehicle_Collisions.csv")
    file = open("Bronx_Car_Accidents.kml", "w")
    data_csv_file = open("Cleaned_Data.csv", "w")
    bronx_data = raw_data[raw_data['BOROUGH'] =='BRONX']
    #write column names to the file
    for x in range(0, 29):
        if(x == 28):
            data_csv_file.write(raw_data.columns[x] + "\n")
        else:
            data_csv_file.write(raw_data.columns[x] + ",")
    for index, row in bronx_data.iterrows():
        date = row['DATE']
        split_data = date.split('/')
        if(split_data[2]=='2018' or split_data[2]=='2017'):
            if(split_data[0] == '06' or split_data[0] == '07'):
                for x in range(0,29):
                    #write out the row data
                    if(x == 28):
                        data_csv_file.write(str(row[x]) + "\n")
                    else:
                        if(isinstance(row[x],str)):
                            data_csv_file.write(row[x] + ",")
                        else:
                            data_csv_file.write(str(row[x]) + ",")


   
main()