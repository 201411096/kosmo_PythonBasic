### 모듈 ###
#1 3
#2 3
#3 import fah_converter as fah
#4 2
#5 from calculator.py import *
### 파이썬 스타일 코드2 ###
#1 f = lambda x, y : x**y
#2 print("lambda map 함수", list(map(lambda x: x**2, ex)))
#3 [(1,2,3), (4,5,6), (7,8,9)]
#4 2019-9-6
#5
# def vector_size_check(*args):
#         args_length = len(args[0])
#         for arg in args:
#             if(args_length!=len(arg)):
#                 return False
#         return True
#5_답
# def vector_size_check(*args):
#     return len(set([len(arg) for arg in args])) ==1
#6
# def matrix_addition(*matrix_variables):
#   return [[sum(row) for row in zip(*t)] for t in zip(*matrix_variables)]


def matrix_addition(*matrix_variables):
    return [[sum(row) for row in zip(*t)] for t in zip(*matrix_variables)]

matrix_y = [[2, 5], [2, 1]]
matrix_z = [[2, 4], [5, 3]]
matrix_addition(matrix_y, matrix_z)

print("matrix_y와 matrix_z를 zip 한 결과를 확인", list(zip(matrix_y, matrix_z)))
print("matrix_y와 matrix_z를 zip 한 결과의 len 확인", len(list(zip(matrix_y, matrix_z))))
print("matrix_y와 matrix_z를 zip 한 결과 0번 확인", list(zip(matrix_y, matrix_z))[0])
print("matrix_y와 matrix_z를 zip 한 결과 1번 확인", list(zip(matrix_y, matrix_z))[1])
print("matrix_y와 matrix_z를 zip 한 결과 0번을 다시 zip 확인", list(zip(list(zip(matrix_y, matrix_z))[0])))
print("matrix_y와 matrix_z를 zip 한 결과 1번을 다시 zip 확인", list(zip(list(zip(matrix_y, matrix_z))[1])))



"""
#3
def transpose_list(two_dimensional_list):
    return [row for row in zip(*two_dimensional_list)]
transpose_list([[1, 4, 7], [2, 5, 8], [3, 6, 9]])

#6
def matrix_addition(*args):
    #행렬을 더할 함수를 만들어야 함

matrix_y = [[2, 5], [2, 1]]
matrix_z = [[2, 4], [5, 3]]
matrix_addition(matrix_y, matrix_z)
[[4, 9], [7, 4]]
"""