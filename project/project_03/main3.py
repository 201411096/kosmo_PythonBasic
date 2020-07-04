import storedb
import folium
# 모든 지점 정보를 가져와서 지도에 표시

datalist = storedb.select_data()    # 모든 지점의 주소를 가져와서 저장
addrList = []   # 마커의 x, y좌표들를 담을 리스트
nameList = []   # 마커의 지점 이름을 담을 리스트

# datalist -> (지점 이름, 지점 주소)을 담을 튜플들을 담을 리스트
for idx, data in enumerate(datalist):
    # 지점의 주소(string)을 위도 경도로 변환
    addr = storedb.conversion(data[1])
    # 주소->좌표 변환로 변환시 좌표값이 나오지 않은 경우
    if addr is None:
        continue
    # 주소가 좌표료 변환되었다면 좌표를 담는 리스트와 지점 이름을 담는 리스트에 추가
    addrList.append(addr)
    nameList.append(data[0])



# 지도의 포커스를 맨 처음 리스트에 담긴 매장 위치를 기준으로 설정
map_osm = folium.Map(location=[addrList[0]['y'], addrList[0]['x']], zoom_start=10)


# 주소리스트에 담긴 x,y좌표에 마커를 지도에 표시 (popup시 지점 이름리스트에 담긴 이름들이 표기)
for idx, conversiondata in enumerate(addrList):
    folium.Marker(location=[addrList[idx]['y'], addrList[idx]['x']], 
                  popup=nameList[idx], icon=folium.Icon(color="red", icon="info-sign")).add_to(map_osm)


# 지점들의 위치가 표시된 지도를 파일로 저장
map_osm.save("./map/result.html")



