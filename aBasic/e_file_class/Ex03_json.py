#Ex03_json.py
import json

f = open('data/temp.json', 'r', encoding='utf-8')
data = f.read()
print(data)
print('-'*50)

items = {}
items = json.loads(data)
print(type(items)) # json.loads 딕셔너리 형태로 반환해줌
print(items)

for item in items:
    print('>', item)

for item in items.values():
    print('>', item)

for item in items.items():
    print('>', item)