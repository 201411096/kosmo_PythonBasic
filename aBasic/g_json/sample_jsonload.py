# json.load 예시

import json

file_path = './sample.json'


with open(file_path, 'r') as targetfile:
    val1 = json.load(targetfile)
print(val1)
print(type(val1))

targetfile = open(file_path, 'r')
val2 =targetfile.read()

print(val2)         # ...
print(type(val2))   # str
val3 = json.loads(val2)
print(val3)         # 한 줄로 나옴
print(type(val3))   # dict (type이 json으로 나오지는 않음)

