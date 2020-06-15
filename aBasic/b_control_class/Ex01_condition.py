"""
 [ 제어문 ]
    - 파이썬은 들여쓰기를 하여 블록을 표현한다
    - 들여쓰기는 탭과 공백을 섞어 쓰지 말자

    [ex]
    if a>b:
        print(a)
            print(b)  => 에러발생

    (1) if 문
        if 조건식A :
            문장들
        elif 조건식B :
            문장들
        else :
            문장들

        ` 조건식이나 else 뒤에는 콜론(:) 표시
        ` 조건식을 ( ) 괄호 필요없다
        ` 실행할 코드가 없으면 pass
        ` 파이썬은 switch 문 없음
"""

# 거짓(False)의 값
# 아래 부분은 전부 거짓을 의미함
i = 0;
i2=0.0
i3=""
i4=str()
i5=list()
i6=tuple()
i7=set()
i8=dict()
i9={}
i10=None

#1 숫자에 의한 조건 --------------------
a= -1
if a:
    print('True')
else:
    print('False')

if not i:
    print("True2")
else:
    print("False2")

#2 논리 연산자를 이용한 조건 --------------------
a = 10
b = -1
if a and b:
    print('True3')
if a or b:
    print('True4')

# 정리필요
# 아래 예문은 유사 short-circuit logic이 적용?...
print(a and b)  # -1 출력
# and operation 시에 앞의 값이 false라면 앞의 값이 출력이 되지만 logic이 전체적으로 true라면 중요도에 따라서 가장 마지막 값이 출력됨
print(a or b)   # 10 출력

#3 find() : 찾으면 해당하는 인덱스를 반환하고 못 찾으면 -1을 반환
word = 'korea'
if word.find('k'):      # 0 -> False => 찾은 인덱스값이 0이기때문에 false로 취급하여 print부분을 출력하지 않음
    print('1>' + word)
if word.find('z'):      # -1 -> True => 찾은 값이 없이 -1을 반환하기 때문에 True로 취급하여 print부분을 출력함
    print('2>' + word)

word = 'korea'
if word.find('k') >= 0: # -1 보다 큰 경우에만 출력을 하도록.. # >-1로 하는 것이 일반적인듯
    print('1>' + word)
if word.find('z') >= 0: # -1 보다 큰 경우에만 출력을 하도록.. # >-1로 하는 것이 일반적인듯
    print('2>' + word)