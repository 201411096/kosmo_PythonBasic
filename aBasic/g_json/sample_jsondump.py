# json.dump 예시

import json

file_path = './sample.json'

# json으로 저장하고 싶은 변수
val1 = {
    'key1': ['a', 'b', 'c'],
    'key2': {
        'key2_1':('aa', 'bb'),
        'key2_2':('cc', 'dd', 'ee'),
        'key2_3':([1,2,3], [4,5,6])
    },
    'key3': ('aaa', 'bbb', 'ccc')
}

print(val1)
print(type(val1))

with open(file_path, 'w') as targetfile:
    json.dump(val1, targetfile, indent=4)


# json.dumps 예시
print(val1)       # {'key1': ['a', 'b', 'c'], 'key2': {'key2_1': ('aa', 'bb'), 'key2_2': ('cc', 'dd', 'ee'), 'key2_3': ([1, 2, 3], [4, 5, 6])}, 'key3': ('aaa', 'bbb', 'ccc')}
val2 = json.dumps(val1)
print(val2)       # {"key1": ["a", "b", "c"], "key2": {"key2_1": ["aa", "bb"], "key2_2": ["cc", "dd", "ee"], "key2_3": [[1, 2, 3], [4, 5, 6]]}, "key3": ["aaa", "bbb", "ccc"]}
print(type(val2)) # str