import storedb
import folium
from selenium import webdriver

# name = str(input("이름 입력"))
# addr = storedb.selectOne_data(name)

addr = storedb.selectOne_data()

data = storedb.conversion(addr)
print(data['x'], data['y'])

# 방법 1
#driver = webdriver.Chrome('./webdriver/chromedriver')
#driver.implicitly_wait(3)

#driver.get('https://map.kakao.com/link/map/{},{}'.format(data['y'], data['x']))
#driver.get('https://map.kakao.com/link/map/{}'.format(data['b_code']))

# 방법 2
map_osm = folium.Map(location=[data['y'], data['x']], zoom_start=17)
folium.Marker(location=[data['y'], data['x']],
              popup=data['address_name'],
              icon=folium.Icon(color="red", icon="info-sign")).add_to(map_osm)
#folium.CircleMarker(location=[37.572463, 126.975611], popup="광화문역", radius=100, color="red", fill_color="#AAAA33").add_to(map_osm)
map_osm.save("./map/"+data['address_name']+'.html')