from pprint import pprint

import pandas as pd
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
import numpy as np


# Get the data
data2017 = pd.read_csv("Cleaned_2017.csv")
data2018 = pd.read_csv("Cleaned_2018.csv")
# Get the injury and death rows
data_2017 = data2017[["NUMBER OF PERSONS INJURED","NUMBER OF PERSONS KILLED", "NUMBER OF PEDESTRIANS INJURED","NUMBER OF PEDESTRIANS KILLED","NUMBER OF CYCLIST INJURED","NUMBER OF CYCLIST KILLED","NUMBER OF MOTORIST INJURED","NUMBER OF MOTORIST KILLED"]]
data_2018 = data2018[["NUMBER OF PERSONS INJURED","NUMBER OF PERSONS KILLED", "NUMBER OF PEDESTRIANS INJURED","NUMBER OF PEDESTRIANS KILLED","NUMBER OF CYCLIST INJURED","NUMBER OF CYCLIST KILLED","NUMBER OF MOTORIST INJURED","NUMBER OF MOTORIST KILLED"]]


def process_data(data_set):
    """
    Process the injury and death data
    :param data_set: The data set to process
    :return: the processed data
    """
    result1 = {
                 "NUMBER OF PERSONS INJURED": 0,
                 "NUMBER OF PERSONS KILLED": 0,
    }

    result2 = {
                 "NUMBER OF PEDESTRIANS KILLED": 0,
                 "NUMBER OF MOTORIST KILLED": 0,
                 "NUMBER OF CYCLIST KILLED": 0
    }

    result3 = {
                 "NUMBER OF PEDESTRIANS INJURED": 0,
                 "NUMBER OF MOTORIST INJURED": 0,
                 "NUMBER OF CYCLIST INJURED": 0
    }

    for row in data_set:
        result1["NUMBER OF PERSONS INJURED"] += row[0]
        result1["NUMBER OF PERSONS KILLED"] += row[1]

        result3["NUMBER OF PEDESTRIANS INJURED"] += row[2]
        result2["NUMBER OF PEDESTRIANS KILLED"] += row[3]
        result3["NUMBER OF CYCLIST INJURED"] += row[4]
        result2["NUMBER OF CYCLIST KILLED"] += row[5]
        result3["NUMBER OF MOTORIST INJURED"] += row[6]
        result2["NUMBER OF MOTORIST KILLED"] += row[7]
    return [result1, result2, result3]


# Process the data
graph_data_2017 = process_data(data_2017.values)
graph_data_2018 = process_data(data_2018.values)

def labelBars(rects):
    """
    Labels the bars on graphs with values
    :param rects:
    :return:
    """
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h), ha='center', va='bottom', fontsize=12)

# Graph number of injuries
fig, ax = plt.subplots()

index = np.arange(1)
bar_width = 0.35

opacity = 0.4
error_config = {'ecolor': '0.3'}

bars1 = ax.bar(index, graph_data_2017[0]["NUMBER OF PERSONS INJURED"], bar_width,
               alpha=opacity, color='b',label='2017')

bars2 = ax.bar(index + bar_width, graph_data_2018[0]["NUMBER OF PERSONS INJURED"], bar_width,
               alpha=opacity, color='r', label='2018')

labelBars(bars1)
labelBars(bars2)

font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 10,
        }

ax.set_xlabel("NUMBER OF PERSONS INJURED")
ax.set_ylabel('Number Of Occurrences')
ax.set_title('Injuries In 2017 VS 2018')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels("", fontdict=font, rotation=90)
ax.legend()

fig.tight_layout()
plt.show()
#####################################################################
# Graph number of deaths

fig, ax = plt.subplots()

index = np.arange(1)
bar_width = 0.35

opacity = 0.4
error_config = {'ecolor': '0.3'}

bars1 = ax.bar(index, graph_data_2017[0]["NUMBER OF PERSONS KILLED"], bar_width,
               alpha=opacity, color='b',label='2017')

bars2 = ax.bar(index + bar_width, graph_data_2018[0]["NUMBER OF PERSONS KILLED"], bar_width,
               alpha=opacity, color='r', label='2018')
labelBars(bars1)
labelBars(bars2)
font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 10,
        }

ax.set_xlabel("NUMBER OF PERSONS KILLED")
ax.set_ylabel('Number Of Occurrences')
ax.set_title('Deaths In 2017 VS 2018')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels("", fontdict=font, rotation=90)
ax.legend()

fig.tight_layout()
plt.show()

#####################################################################
# Graph number of specific death types

fig, ax = plt.subplots()

index = np.arange(len(graph_data_2018[1].keys()))
bar_width = 0.35

opacity = 0.4
error_config = {'ecolor': '0.3'}

bars1 = ax.bar(index, graph_data_2017[1].values(), bar_width,
               alpha=opacity, color='b',label='2017')

bars2 = ax.bar(index + bar_width, graph_data_2018[1].values(), bar_width,
               alpha=opacity, color='r', label='2018')
labelBars(bars1)
labelBars(bars2)
font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 8,
        }

ax.set_ylabel('Number Of Occurrences')
ax.set_title('People Killed In 2017 VS 2018')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(graph_data_2018[1].keys(), fontdict=font, rotation=45)
ax.legend()

fig.tight_layout()
plt.show()

#####################################################################
# Graph number of specific death types

fig, ax = plt.subplots()

index = np.arange(len(graph_data_2018[2].keys()))
bar_width = 0.35

opacity = 0.4
error_config = {'ecolor': '0.3'}

bars1 = ax.bar(index, graph_data_2017[2].values(), bar_width,
               alpha=opacity, color='b',label='2017')

bars2 = ax.bar(index + bar_width, graph_data_2018[2].values(), bar_width,
               alpha=opacity, color='r', label='2018')
labelBars(bars1)
labelBars(bars2)
font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 8,
        }

ax.set_ylabel('Number Of Occurrences')
ax.set_title('People Injured In 2017 VS 2018')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(graph_data_2018[2].keys(), fontdict=font, rotation=45)
ax.legend()

fig.tight_layout()
plt.show()