import numpy as np

origin = np.array([3,1,9,7])
print('원본:', origin)


sorted = origin.sort()
print('원본:', origin)
print('정렬 후 :', sorted)
sorted2 = np.sort(origin)[::-1] # 모든 행, 모든 열에서 -1 을 추가로 표기하면 내림차순이 되버림
print('내림차순', sorted2)

np.linspace()