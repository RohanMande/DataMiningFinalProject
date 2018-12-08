from pprint import pprint

import pandas as pd
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
import numpy as np

data2017 = pd.read_csv("Cleaned_2017.csv")
data2018 = pd.read_csv("Cleaned_2018.csv")
t_data_2017 = data2017[['VEHICLE TYPE CODE 1', 'VEHICLE TYPE CODE 2', 'VEHICLE TYPE CODE 3', 'VEHICLE TYPE CODE 4', 'VEHICLE TYPE CODE 5']]
t_data_2018 = data2018[['VEHICLE TYPE CODE 1', 'VEHICLE TYPE CODE 2', 'VEHICLE TYPE CODE 3', 'VEHICLE TYPE CODE 4', 'VEHICLE TYPE CODE 5']]


def process_types(bike_data):
    vehicle_types = {
        'Fire': 0, 'Moped': 0, 'Ambulance': 0, 'Sports Utility / Station Wagon': 0,
        'Convertible': 0, 'Taxi': 0, '3 Door': 0, 'Motorcycle': 0, 'Flat Bed': 0,
        'Tractor Trailer': 0, 'Bicycle': 0, 'Concrete Truck': 0, 'Mail Truck': 0,
        'Mini Bike': 0, 'Chassis Cab': 0, 'Golf Cart': 0, 'Pickup Truck': 0, 'Van': 0,
        'Snow Plow': 0, 'Livestock Rack': 0, 'Tow Truck': 0, 'Tanker': 0, 'Dump Truck': 0, 'Passenger Vehicle': 0,
        'Garbage Truck': 0, 'Bus': 0, 'Scooter': 0, 'Beverage Truck': 0, 'School Bus': 0, 'Sedan': 0, 'Box Truck': 0,
        'Unknown': 0}

    vehicle_type_data = []
    vehicle_type_totals = vehicle_types.copy()
    general_vehicle_type_totals = {"Passenger Car": 0, "Commercial Vehicle / Truck":0, "Motorcycle / Moped / Bicycle":0, "Bus":0, "Van":0, "Other": 0}
    for index, row in enumerate(bike_data.values):
        vehicle_type_data.append(dict(vehicle_types))
        for vtype in row:
            vtype = str(vtype).lower()
            if 'fire' in vtype or 'fdny' in vtype:
                vehicle_type_data[index]['Fire'] += 1
                vehicle_type_totals['Fire'] += 1
                general_vehicle_type_totals['Commercial Vehicle / Truck'] += 1
            elif 'ambu' in vtype:
                vehicle_type_data[index]['Ambulance'] += 1
                vehicle_type_totals['Ambulance'] += 1
                general_vehicle_type_totals['Commercial Vehicle / Truck'] += 1
            elif 'sports' in vtype or 'station' in vtype:
                vehicle_type_data[index]['Sports Utility / Station Wagon'] += 1
                vehicle_type_totals['Sports Utility / Station Wagon'] += 1
                general_vehicle_type_totals['Passenger Car'] += 1
            elif 'mop' in vtype or 'motors' in vtype:
                vehicle_type_data[index]['Moped'] += 1
                vehicle_type_totals['Moped'] += 1
                general_vehicle_type_totals['Motorcycle / Moped / Bicycle'] += 1
            elif 'convertible' in vtype:
                vehicle_type_data[index]['Convertible'] += 1
                vehicle_type_totals['Convertible'] += 1
                general_vehicle_type_totals['Passenger Car'] += 1
            elif 'box truck' in vtype:
                vehicle_type_data[index]['Box Truck'] += 1
                vehicle_type_totals['Box Truck'] += 1
                general_vehicle_type_totals['Commercial Vehicle / Truck'] += 1
            elif 'tax' in vtype:
                vehicle_type_data[index]['Taxi'] += 1
                vehicle_type_totals['Taxi'] += 1
                general_vehicle_type_totals['Passenger Car'] += 1
            elif '3' in vtype:
                vehicle_type_data[index]['3 Door'] += 1
                vehicle_type_totals['3 Door'] += 1
                general_vehicle_type_totals['Passenger Car'] += 1
            elif 'motorc' in vtype or 'motorb' in vtype:
                vehicle_type_data[index]['Motorcycle'] += 1
                vehicle_type_totals['Motorcycle'] += 1
                general_vehicle_type_totals['Motorcycle / Moped / Bicycle'] += 1
            elif 'flat' in vtype or 'fb' in vtype:
                vehicle_type_data[index]['Flat Bed'] += 1
                vehicle_type_totals['Flat Bed'] += 1
                general_vehicle_type_totals['Commercial Vehicle / Truck'] += 1
            elif 'tract' in vtype or 'tt' in vtype or 'trail' in vtype:
                vehicle_type_data[index]['Tractor Trailer'] += 1
                vehicle_type_totals['Tractor Trailer'] += 1
                general_vehicle_type_totals['Commercial Vehicle / Truck'] += 1
            elif 'conc' in vtype:
                vehicle_type_data[index]['Concrete Truck'] += 1
                vehicle_type_totals['Concrete Truck'] += 1
                general_vehicle_type_totals['Commercial Vehicle / Truck'] += 1
            elif 'mail' in vtype:
                vehicle_type_data[index]['Mail Truck'] += 1
                vehicle_type_totals['Mail Truck'] += 1
                general_vehicle_type_totals['Commercial Vehicle / Truck'] += 1
            elif 'mini' in vtype:
                vehicle_type_data[index]['Mini Bike'] += 1
                vehicle_type_totals['Mini Bike'] += 1
                general_vehicle_type_totals['Motorcycle / Moped / Bicycle'] += 1
            elif 'chass' in vtype:
                vehicle_type_data[index]['Chassis Cab'] += 1
                vehicle_type_totals['Chassis Cab'] += 1
                general_vehicle_type_totals['Commercial Vehicle / Truck'] += 1
            elif 'golf' in vtype:
                vehicle_type_data[index]['Golf Cart'] += 1
                vehicle_type_totals['Golf Cart'] += 1
                general_vehicle_type_totals['Other'] += 1
            elif 'pick' in vtype:
                vehicle_type_data[index]['Pickup Truck'] += 1
                vehicle_type_totals['Pickup Truck'] += 1
                general_vehicle_type_totals['Commercial Vehicle / Truck'] += 1
            elif 'van' in vtype:
                vehicle_type_data[index]['Van'] += 1
                vehicle_type_totals['Van'] += 1
                general_vehicle_type_totals['Van'] += 1
            elif 'snow' in vtype:
                vehicle_type_data[index]['Snow Plow'] += 1
                vehicle_type_totals['Snow Plow'] += 1
                general_vehicle_type_totals['Commercial Vehicle / Truck'] += 1
            elif 'live' in vtype:
                vehicle_type_data[index]['Livestock Rack'] += 1
                vehicle_type_totals['Livestock Rack'] += 1
                general_vehicle_type_totals['Commercial Vehicle / Truck'] += 1
            elif 'tow' in vtype:
                vehicle_type_data[index]['Tow Truck'] += 1
                vehicle_type_totals['Tow Truck'] += 1
                general_vehicle_type_totals['Commercial Vehicle / Truck'] += 1
            elif 'tank' in vtype:
                vehicle_type_data[index]['Tanker'] += 1
                vehicle_type_totals['Tanker'] += 1
                general_vehicle_type_totals['Commercial Vehicle / Truck'] += 1
            elif 'dump' in vtype:
                vehicle_type_data[index]['Dump Truck'] += 1
                vehicle_type_totals['Dump Truck'] += 1
                general_vehicle_type_totals['Commercial Vehicle / Truck'] += 1
            elif 'garb' in vtype:
                vehicle_type_data[index]['Garbage Truck'] += 1
                vehicle_type_totals['Garbage Truck'] += 1
                general_vehicle_type_totals['Commercial Vehicle / Truck'] += 1
            elif 'school' in vtype:
                vehicle_type_data[index]['School Bus'] += 1
                vehicle_type_totals['School Bus'] += 1
                general_vehicle_type_totals['Bus'] += 1
            elif 'beverage' in vtype:
                vehicle_type_data[index]['Beverage Truck'] += 1
                vehicle_type_totals['Beverage Truck'] += 1
                general_vehicle_type_totals['Commercial Vehicle / Truck'] += 1
            elif 'bus' in vtype:
                vehicle_type_data[index]['Bus'] += 1
                vehicle_type_totals['Bus'] += 1
                general_vehicle_type_totals['Bus'] += 1
            elif 'scoot' in vtype:
                vehicle_type_data[index]['Scooter'] += 1
                vehicle_type_totals['Scooter'] += 1
                general_vehicle_type_totals['Motorcycle / Moped / Bicycle'] += 1
            elif 'bic' in vtype or 'bike' in vtype:
                vehicle_type_data[index]['Bicycle'] += 1
                vehicle_type_totals['Bicycle'] += 1
                general_vehicle_type_totals['Motorcycle / Moped / Bicycle'] += 1
            elif 'sedan' in vtype:
                vehicle_type_data[index]['Sedan'] += 1
                vehicle_type_totals['Sedan'] += 1
                general_vehicle_type_totals['Passenger Car'] += 1
            elif 'sports' in vtype or 'station' in vtype:
                vehicle_type_data[index]['Sports Utility / Station Wagon'] += 1
                vehicle_type_totals['Sports Utility / Station Wagon'] += 1
                general_vehicle_type_totals['Passenger Car'] += 1
            elif 'pass' in vtype or 'station' in vtype:
                vehicle_type_data[index]['Passenger Vehicle'] += 1
                vehicle_type_totals['Passenger Vehicle'] += 1
                general_vehicle_type_totals['Passenger Car'] += 1
            elif 'nan' in vtype:
                continue
            else:
                vehicle_type_data[index]['Unknown'] += 1
                general_vehicle_type_totals['Other'] += 1
    return [vehicle_type_data, vehicle_type_totals, general_vehicle_type_totals]


data_2017 = process_types(t_data_2017)
data_2018 = process_types(t_data_2018)

fig, ax = plt.subplots()

index = np.arange(len(data_2018[2].keys()))
bar_width = 0.35

opacity = 0.4
error_config = {'ecolor': '0.3'}

bars1 = ax.bar(index, data_2017[2].values(), bar_width,
                alpha=opacity, color='b',
                label='2017')

bars2 = ax.bar(index + bar_width, data_2018[2].values(), bar_width,
                alpha=opacity, color='r',
                label='2018')

font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 8,
        }

ax.set_xlabel('Vehicle Types')
ax.set_ylabel('Number Of Occurrences In All Accidents')
ax.set_title('General Vehicle Types In 2017 VS 2018')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(data_2018[2].keys(), fontdict=font, rotation=45)
ax.legend()

fig.tight_layout()
plt.show()


#graphing_rows = []
#for dictt in vehicle_type_data:
#    new_row = []
#    for val in dictt.values():
#        new_row.append(int(val))
#    graphing_rows.append(new_row)
#
#graphing_rows = np.asarray(graphing_rows)
#Z = linkage(graphing_rows)
#plt.title('Hierarchical Clustering Dendrogram (truncated)')
#plt.xlabel('sample index')
#plt.ylabel('distance')
#dendrogram(
#    Z,
#    truncate_mode='lastp',  # show only the last p merged clusters
#    p=10,  # show only the last p merged clusters
#    show_leaf_counts=False,  # otherwise numbers in brackets are counts
#    leaf_rotation=90.,
#    leaf_font_size=10)
#plt.show()

#kmeans = KMeans(n_clusters=2).fit(graphing_rows)

fig, ax = plt.subplots()

index = np.arange(len(data_2018[1].keys()))
bar_width = 0.35

opacity = 0.4
error_config = {'ecolor': '0.3'}

bars1 = ax.bar(index, data_2017[1].values(), bar_width,
                alpha=opacity, color='b',
                label='2017')

bars2 = ax.bar(index + bar_width, data_2018[1].values(), bar_width,
                alpha=opacity, color='r',
                label='2018')

font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 7,
        }

ax.set_xlabel('Vehicle Types')
ax.set_ylabel('Number Of Occurrences In All Accidents')
ax.set_title('Specific Vehicle Types In 2017 VS 2018')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(data_2018[1].keys(), fontdict=font, rotation=90)
ax.legend()

fig.tight_layout()
plt.show()