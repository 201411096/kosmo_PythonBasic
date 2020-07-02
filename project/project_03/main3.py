import storedb
import folium
# 모든 매점 정보를 가져와서 지도에 모두 찍음

datalist = storedb.select_data()
addrList = []
nameList = []
for idx, data in enumerate(datalist):
    addr = storedb.conversion(data[1])
    if addr is None: # 문제가 발생하는 행이 있으면 그냥 넘김(주소->좌표 변환을 사용했는데 좌표가 나오지 않은 경우)
        continue
    addrList.append(addr)
    nameList.append(data[1])
map_osm = folium.Map(location=[addrList[0]['y'], addrList[0]['x']], zoom_start=10) #처음 지도 포커스를 맨 처음 매장 위치를 기준으로 잡음
for idx, conversiondata in enumerate(addrList):
    folium.Marker(location=[addrList[idx]['y'], addrList[idx]['x']], popup=nameList[idx], icon=folium.Icon(color="red", icon="info-sign")).add_to(map_osm) #매장개수만큼 매장의 위치를 마커로 표시

map_osm.save("./map/result.html") # 해당 지도를 파일로 저장