# 제어문
# 1. fruit -> apple (마지막 조건에서 문자열이 아닌 자기 자신을 넣음)
# 2. 3 4 -> [3, 4.0]
# 3. 2 -> 5 (문제 잘 안봄)
# 4. -4 -> -5 (range의 마지막(stop)은 실행하지 않음)
# 5. 135689 -> 986531 (문제 잘 안봄)
# 6. 1800
# 7. error -> 6 (.?)
# 파이썬 스타일 코드
# 1. 3
# 2. 2 -> dictionary 이기 떄문에 똑같은 단어가 들어오면 덮어쓰기가 되버림, +++ 순서는 그대로 유지되면서 덮어쓰기가 됨
# 3. ? -> orange&pink&brown&black&white
#   ㄴ str1.join(arr1) : arr1 사이사이에 str1을 넣어서 붙임
# 4. {'students': 0, 'superuser': 1, 'professor': 2, 'employee': 3}
# 6. Cat panda Owl -> ['Cat', 'Panda', 'Owl']
# 7. Hong Gil University ->  DongUniversity (실수)
# 8.
# 9. [[12, 3], [15, 3], [12, 2]] -> [[12, 3], [15, 3]]
# 10. tue, yellow -> yellow (2차원 배열 식으로 묶임, key value식으로 묶이는 게 아님)


week = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']

list_data = [week, rainbow]

print(list_data)

"""

"""

"""
---------------문제---------------
# 파이썬 스타일 코드
3.
    colors = ['orange', 'pink', 'brown', 'black', 'white']
    result = '&'.join(colors)
    print(result)
9.
a = [1, 2, 3]
b = [4, 5, ]
c = [7, 8, 9]
print([[sum(k), len(k)] for k in zip(a, b, c)])
-> 부족한 부분은 아예 zip이 되지 않음
---------------문제---------------
"""