"""
    [ 함수 ]

     반복적인 구문을 만들어 함수로 선언하여 간단하게 호출만 하고자 한다

     def 함수명(매개변수):
        수행할 문장들
"""

# (1) 인자도 리턴값도 없는 함수
def func():
    print('확인')

func()
print(func()) # 리턴값이 없는 경우 none이 반환됨

# (2) 리턴값이 여러개 가능 => 리턴값이 여러개라면 튜플로 만들어서 반환해줌
def func(arg1, arg2):
    return arg1+5, arg2*2

print(func(5,3))
a, b = func(2, 4)
print(a, b)
print(a+b)

# (3) 위치인자(positional argument)
def func(greeing, name="아무개"):
    print('{0} !!!!!! {1}님'.format(greeing, name))

func("hello", '홍씨')
func("김씨", '안녕')

# (4) 키워드 인자(keyward argument)
func(name="김씨", greeing='안녕')

# (5) 매개변수의 기본값 지정하기
func('올라')

def func(a, b, c=100):
    return a+b+c
result = func(10, 20, 30)
print("result1값 확인 :", result)
result = func(10, 20)
print("result2값 확인 :", result)

def buggy(arg, result=[]):
    result.append(arg)
    print(result)
buggy('A')
buggy('B')
buggy('Z', [1,2,3,4])
buggy('가')

# (6) 위치인자 모으기 (*args)
'''
1번째와 2번째는 인자가 반드시 들어가고 3번째는 인자가 들어갈 수도 있고 없으면 0으로 초기화한다
그러나 4번째 인자부터는 정확히 모른다면?
print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))       # args에 7,8,9가 튜플로 들어간다
'''
# *args 부분에 튜플형태로 들어옴
def func(a, b, c=0, *args):
    sum = a+b+c
    for i in args:
        sum+=i
    return sum

print("#6 위치인자 모으기 확인", func(4, 5))
print("#6 위치인자 모으기 확인", func(4, 5, 6))
print("#6 위치인자 모으기 확인", func(4, 5, 6, 7))
print("#6 위치인자 모으기 확인", func(4, 5, 6, 7, 8, 9))       # args에 7,8,9가 튜플로 들어간다

# (7) 키워드 인자 모으기 (**kwargs)

# def func(i, j, k=100, *args, **kwargs):
#     print()
#     print("#7 키워드 인자 모으기 확인", i+j+k)
#     print("#7 키워드 인자 모으기 확인", args)
#     print("#7 키워드 인자 모으기 확인", kwargs)
# func(10, 20)
# func(1, 2, 3)
# func(1, 2, 3, 4, 5, 6)
# func(1, 2, 3, 4, a=10, b=20, c=30)

# 넘어오는 인자의 값들을 모두 합산한 값을 리턴

def func(i, j, k=100, *args, **kwargs):
    sum=i+j+k
    print(kwargs)
    for temp1 in args:
        sum+=temp1
    for temp2 in kwargs.values():
        sum+=temp2
    return sum

print(func(10, 20))
print(func(1, 2, 3))
print(func(1, 2, 3, 4, 5, 6))
print(func(1, 2, 3, 4, a=10, b=20, c=30))
print(func(1, 2, 3, 4, a=10, z=30))