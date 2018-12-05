import pandas as pd



def main():
    file = open("Bronx_Car_Accidents.kml", "w")
    crash_data = pd.DataFrame()
    crash_data = pd.read_csv("Cleaned_Data.csv",index_col=False)
    header_string = "<?xml version=" + chr(34) + "1.0" + chr(34) + " encoding=" + chr(34) + "UTF-8" + chr(34) + "?>\n"
    header_string = header_string + "<kml xmlns=" + chr(34) + "http://www.opengis.net/kml/2.2" + chr(34) + ">\n"
    header_string = header_string + "<Document>\n"
    file.write(header_string)
    for index, row in crash_data.iterrows():
        file.write("\t<Placemark>\n")
        file.write("\t\t<name>Crash</name>\n")
        file.write("\t\t<Point>\n")
        file.write("\t\t\t<coordinates>" + str(row[5]) + "," + str(row[4]) + "</coordinates>\n")
        file.write("\t\t</Point>\n")
        file.write("\t</Placemark>\n")
    file.write("</Document>\n")
    file.write("</kml>")
main()