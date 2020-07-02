import storedb
import folium

datalist = storedb.select_data()
addrList = []
for idx, data in enumerate(datalist):
    #print(data)
    addr = storedb.conversion(data[1])
    if addr is None:
        del datalist[idx]
        continue
    addrList.append(addr)
    print("main3.py ", idx, "addr 확인", addr)
print("addrList확인", addrList)
print("datalist 확인", datalist)
map_osm = folium.Map(location=[addrList[0]['y'], addrList[0]['x']], zoom_start=5)
for idx, conversiondata in enumerate(addrList):
    folium.Marker(location=[addrList[idx]['y'], addrList[idx]['x']], popup=datalist[idx][1], icon=folium.Icon(color="red", icon="info-sign")).add_to(map_osm)
map_osm.save("./map/result.html")