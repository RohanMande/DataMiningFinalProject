#This class is takes all of the data from the bronx and creates a KML file showing where there were crashes
import pandas as pd
import sys
import numpy as np





def main():
    raw_data = pd.DataFrame()
    raw_data = pd.read_csv("NYPD_Motor_Vehicle_Collisions.csv")
    data_csv_file = open("Cleaned_Data.csv", "w")
    bronx_data = raw_data[raw_data['BOROUGH'] =='BRONX']
    csv_2017=  open("Cleaned_2017.csv", "w")
    csv_2018 = open("Cleaned_2018.csv", "w")
#    write column names to the file
    #data_csv_file.write("ID,")
    for x in range(0, 29):
        if(x == 28):
            data_csv_file.write(raw_data.columns[x] + "\n")
            csv_2017.write(raw_data.columns[x] + "\n")
            csv_2018.write(raw_data.columns[x] + "\n")
        else:
            data_csv_file.write(raw_data.columns[x] + ",")
            csv_2017.write(raw_data.columns[x] + ",")
            csv_2018.write(raw_data.columns[x] + ",")
    row_num = 0
    for index, row in bronx_data.iterrows():

        date = row['DATE']
        split_data = date.split('/')
        # if(split_data[2]=='2018' or split_data[2]=='2017'):
        #     if(split_data[0] == '06' or split_data[0] == '07'):
        #         if(not(np.isnan(row['LONGITUDE'] or np.isnan(row['LATITUDE'])))):
        #             for x in range(0,29):
        #                 # if(x==0):
        #                 #     data_csv_file.write(str(row_num) + ",")
        #                 #     row_num = row_num +1
        #                 #write out the row data
        #                 if(x == 28):
        #                     data_csv_file.write(str(row[x]) + "\n")
        #                 else:
        #                     if(isinstance(row[x],str)):
        #                         data_csv_file.write(row[x] + ",")
        #                     else:
        #                         data_csv_file.write(str(row[x]) + ",")
        if(split_data[2] == '2018'):
            if(split_data[0] == '06' or split_data[0] == '07'):
                if (not (np.isnan(row['LONGITUDE'] or np.isnan(row['LATITUDE'])))):
                    for x in range(0, 29):
                        if( x==28):
                            csv_2018.write(str(row[x]) + "\n")
                        else:
                            if (isinstance(row[x], str)):
                                csv_2018.write(row[x] + ",")
                            else:
                                csv_2018.write(str(row[x]) + ",")
        elif(split_data[2] == '2017'):
            if(split_data[0] == '06' or split_data[0]=='07'):
                if (not (np.isnan(row['LONGITUDE'] or np.isnan(row['LATITUDE'])))):
                    for x in range(0,29):
                        if(x==28):
                            csv_2017.write(str(row[x]) + "\n")
                        else:
                            if (isinstance(row[x], str)):
                                csv_2017.write(row[x] + ",")
                            else:
                                csv_2017.write(str(row[x]) + ",")
    data_csv_file.close()
    csv_2017.close()
    csv_2018.close()


   
main()