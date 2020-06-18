# 1.
# class Calculator:
#     list=[]
#     def __init__(self, list):
#         self.list = list
#     def sum(self):
#         print(sum(self.list))
#     def avg(self):
#         print(sum(self.list)/len(self.list))
# cal = Calculator([1,2,3,4,5])
# cal.sum()
# cal.avg()

# 2.
# kor_score = int(input("국어 점수를 입력->"))
# eng_score = int(input("영어 점수를 입력->"))
# math_score = int(input("수학 점수를 입력->"))
# total = kor_score+eng_score+math_score
# avg = total / 3
# print("총점 : {0}, 평균{1}".format(total, avg))

# 3.
# def product(num, list):
#     return [element*num for element in list]
# print(product(5, [1,2,3,4,5]))

# 4.
# def matrix_add(*matrix_variables):
#     return [[sum(row) for row in zip(*t)] for t in zip(*matrix_variables)]
#
# matrix_x = [[2, 5], [2, 1]]
# matrix_y = [[2, 4], [5, 3]]
# matrix_add(matrix_x, matrix_y)
# print(matrix_add(matrix_x, matrix_y))

# 5.
# def vector_sub(*vector_variable):
#     vector_variables = vector_variable[0]
#     first_variable = vector_variable[0][0]
#     for idx, variable in enumerate(vector_variables):
#         if idx==0:
#             continue
#         first_variable[0] = first_variable[0]-variable[0]
#         first_variable[1] = first_variable[1] - variable[1]
#     return first_variable
# print(vector_sub([[1,3],[2,4]]))
# print(vector_sub([[1,5],[10,4],[4,7]]))