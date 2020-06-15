"""
    [ 콘솔 입력 처리 함수 ]
    - input() : 기본적으로 문자열로 입력받음
    - eval() : 함수로 감싸면 숫자 처리됨 (권장하지 않음)
"""
# # 이름 입력받기
# name = input("이름을 입력")
# print("당신의 이름은 {0}입니다.".format(name))
# print("당신의 이름은 %s입니다." % name)
#
# # 나이와 키를 입력받아 출력하기
# age = input("나이를 입력")
# height = input("키를 입력")
# print("당신의 나이는 {0}입니다.".format(age))
# print("당신의 키는 %s입니다." % height)

#format 함수 요소 확인
# a = 111.123456789
# b = 222.987654321
# print("format 확인1 {1:1.2f}, format 확인2 {0:1.2f}".format(a, b))

#eval 확인
# print('1+2')
# print(eval('1+2'))

#----------------------------------
# 단을 입력받아 구구단을 구하기
# dan = int(input('단 입력 ->'))
#
# for i in range(1, 10): # range(1,10) : 1 ~ 10-1
#     print("{0} * {1} = {2}".format(dan, i, dan*i))

#-----------------------------------------
# print() 함수
print('친구' + '안녕') # 문자열 연결
print('친구', '안녕') # ,로 연결하면 띄어쓰기가 됨
print('친구' '안녕')

# for i in range(1, 6):
#     print("{0}".format(i))
# ln 없이(개행 없이) 하고싶을 경우 end= .. 사용
for i in range(1, 6):
     print(i, end=' ')
# for i in range(5):
#     print("{0}".format(i+1))
# -------------------------------------------------------
# 명령행 매개변수 받기 - java의 main() 함수의 인자
# [ 콘솔에서 실행 ] python Ex10_stdio.py ourserver scott tiger
#                                   0         1      2      3

import sys
args = sys.argv[1:] #메인함수 인자들을 받아옴(파일명을 제외한)
print(args[0], '서버에 연결합니다.')