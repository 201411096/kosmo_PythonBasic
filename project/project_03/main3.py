import storedb
import folium

datalist = storedb.select_data()
addrList = []
nameList = []
for idx, data in enumerate(datalist):
    addr = storedb.conversion(data[1])
    if addr is None:
        continue
    addrList.append(addr)
    nameList.append(data[1])
map_osm = folium.Map(location=[addrList[0]['y'], addrList[0]['x']], zoom_start=10)
for idx, conversiondata in enumerate(addrList):
    folium.Marker(location=[addrList[idx]['y'], addrList[idx]['x']], popup=nameList[idx], icon=folium.Icon(color="red", icon="info-sign")).add_to(map_osm)
map_osm.save("./map/result.html")