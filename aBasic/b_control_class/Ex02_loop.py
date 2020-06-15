
# ------------------------------------------------------
"""
   (2) for문
        for <타켓변수> in 집합객체 :
            문장들
        else:
            문장들

        ㄴ 반복문 뒤에 else는 반복하는 조건에 만족하지않으면 실행 ( 반복분 조건에 맞지 않을 경우에 실행)
            ㄴ 임의로 반복문을 탈출할 경우(ex) 반복문 안에서의 break..) 반복문 else문은 실행되지않음

   (3) while 문
        while 조건문 :
            문장들
        else :
            문장들

        ㄴ 반복문 뒤에 else는 반복하는 조건에 만족하지않으면 실행 ( 반복분 조건에 맞지 않을 경우에 실행)
            ㄴ 임의로 반복문을 탈출할 경우(ex) 반복문 안에서의 break..) 반복문 else문은 실행되지않음
"""
a = 112                  # 숫자형
b = ['1','2','3']       # 리스트
c = '987'                # 문자열
d = tuple(b)             # 튜플
e = dict(k=5, j=6)       # 딕셔너리

for entry in e: # a는 반복이 안되지만 b부터 e까지는 반복된다.
   print(entry)

# 문자열도 하나씩 끊어서 출력해줌 ex) '987' -> 9 8 7
#   딕셔너리 출력시 value값이 아닌 key값들을 출력해줌
#      ㄴ 딕셔너리의 value값을 출력하고 싶을 경우 items()함수 사용을 해야함
#            for entry in e.items: # a는 반복이 안되지만 b부터 e까지는 반복된다.
#            print(entry)

for entry in e.items():
    print(entry)
    print('key=',entry[0], 'value=',entry[1])   # entry의 경우 key value로 되어있던 딕셔너리를 튜플의 형태로 key value 쌍으로 하나씩 가져오기 떄문..

#연습1 1~10까지의 합 출력
sum01 = 0
sum02 = 0
for num in range(1, 11): # range 맨 뒤에껀 포함 안됨
    sum01 += num
print("연습1 결과 출력", sum01)

#연습2 1~10까지의 홀수의 합 출력
for num in range(1, 11):
    if num %2 == 1:
        sum02 += num
print("연습2 결과 출력", sum02)

#연습3 2단부터 9단까지 구구단 출력
print("연습3 결과 출력 --------------------")
for dan in range(2, 10):
    for num in range(1, 10):
        print("{0} * {1} = {2}".format(dan, num, dan*num))







# =========================================================
# while

# a = 1
# while True:  # 무한루프
#    if a == 1:
#        print(a)
#        break


a = ['x', 'y', 'z']
while a:
    data = a.pop()
    print(data)
    if data == 'y':         # 임의로 반복문을 탈출할 경우 반복문 else문은 실행되지않음
        break
else:
    print('end')






"""
[과제] 2단부터 9단까지 이중 반복문으로 출력
"""
