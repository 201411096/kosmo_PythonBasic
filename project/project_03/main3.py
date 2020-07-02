import storedb
import folium

datalist = storedb.select_data()
conversiondatalist = []
for idx, data in enumerate(datalist):
    print(data)
    addr = storedb.conversion(data[1])
    if addr is None:
        continue
    conversiondatalist.append(data)
    print("main3.py ", idx, "addr 확인", addr)