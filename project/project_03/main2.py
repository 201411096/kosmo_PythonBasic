import storedb
import folium
from selenium import webdriver
## 매점 이름 하나를 입력 받아서 마커를 찍음 

addr = storedb.selectOne_data()

data = storedb.conversion(addr)
print(data['x'], data['y'])

# 방법 1 -> 마커가 찍히지 않음
#driver = webdriver.Chrome('./webdriver/chromedriver')
#driver.implicitly_wait(3)

#driver.get('https://map.kakao.com/link/map/{},{}'.format(data['y'], data['x']))
#driver.get('https://map.kakao.com/link/map/{}'.format(data['b_code']))

# 방법 2
map_osm = folium.Map(location=[data['y'], data['x']], zoom_start=17)
folium.Marker(location=[data['y'], data['x']],
              popup=data['address_name'],
              icon=folium.Icon(color="red", icon="info-sign")).add_to(map_osm)
map_osm.save("./map/"+data['address_name']+'.html')