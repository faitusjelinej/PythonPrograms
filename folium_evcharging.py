# Mapping with Python & Folium - Creating Maps from Raw CSV/JSON Data

import csv

filename = '/Users/faitusjelinejoseph/Downloads/Electric_Vehicle_Charging_Stations.csv'
keys = ('Station Name','New Georeferenced Column')
records = []
with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        records.append({key: row[key] for key in keys})

# print(records[0])


for record in records:
    long, lat = record['New Georeferenced Column'].split("(")[-1].split(")")[0].split()
    record['longitude'] = float(long) 
    record['latitude'] = float(lat)   

# records[0]

import folium
from folium.plugins import FastMarkerCluster

latitudes = [a['latitude'] for a in records]
longitudes = [a['longitude'] for a in records]

# for record in records:
#     coords = (record['latitude'],record['longitude'])
#     folium.Marker(coords,popup = record["Station Name"]).add_to(map)
    

FastMarkerCluster(data = list(zip(latitudes,longitudes))).add_to(map)   

print(map)