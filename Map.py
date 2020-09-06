import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
eliv = list(data["ELEV"])
map = folium.Map(location=[38.58,-99.09],zoom_start=6)
fg = folium.FeatureGroup(name="My Map")

def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"


for lt, ln, el in zip(lat,lon, eliv):
    fg.add_child(folium.CircleMarker(location=[lt, ln],radius = 6, popup = str(el)+ " M", fill_color = color_producer(el), color = "grey", fill_opacity = 0.7))

fg.add_child(folium.GeoJson(data = open('world.json','r',encoding = 'utf-8-sig').read()))

map.add_child(fg)
map.save("Map1.html")
