import storedb

#datas = storedb.select_data()
#conversionData = storedb.conversion(datas)

# for data in datas:
#     storedb.conversion()

name = str(input("이름 입력"))
addr = storedb.selectOne_data(name)
print(len(addr))
print(addr[0][1])
#print(storedb.conversion(addr[0][1]))
print(storedb.conversion(addr[0][1]))
print(type(storedb.conversion(addr[0][1])))
