"""
    @ 컴프리핸션 (comprehension)
    ` 하나 이상의 이터레이터로부터 파이썬 자료구조를 만드는 컴팩트한 방법
    ` 비교적 간단한 구문으로 반복문과 조건 테스트를 결합

    * 리스트 컨프리핸션
        [ 표현식 for 항목 in 순회가능객체 ]
        [ 표현식 for 항목 in 순회가능객체 if 조건 ]

    * 딕셔러리 컨프리핸션
        { 키_표현식: 값_표현식 for 표현식 in 순회가능객체 }

    * 셋 컨프리핸션
        { 표현식 for 표현식 in 순회가능객체 }

    ***** tuple comprehension 은 존재하지 않음
"""


# 컨프리핸션 사용하지 않은 리스트 생성
alist = []
alist.append(1)
alist.append(2)
alist.append(3)
alist.append(4)
alist.append(5)
alist.append(6)
print(alist)

alist = []
for n in range(1, 7):
    alist.append(n)
print(alist)

alist = list(range(1, 7))
print(alist)


#------------------------------------------------
# 리스트 컨프리핸션
blist = [n for n in range(1, 7)] # 1부터 6까지 뽑은 값으로 blist를 구성함
print("blist1 =", blist)
blist = [n**2 for n in range(1, 7) if n%2==1] #조건문을 먼저 체크하고 자승을 하는듯?
print("blist2 =", blist)

rows = range(1, 4) # 1,2,3
cols = range(1, 3) # 1,2
dlist = [(r,c) for r in rows for c in cols]
print( "dlist = ", dlist)
#-------------------------------------------
# 딕셔러니 컨프리핸션
data = (2, 3, 4)
a = {x: x**2 for x in data}
print(a)

word = 'LOVE LOL'
wcnt = {letter: word.count(letter) for letter in word}
print(wcnt)
#------------------------------------------------
# 셋 컨프리핸션

# 1부터 6까지 수 중에서 짝수만 셋에 담기
# data03 = (1,2,3,4,5,6)
#data03 = range(1, 7)
data03 = [1,2,3,4,5,4,2,6] # 마지막 결과형태인 set을 따라서 2,4,6이 한번씩만 출력이 됨
set01 = {x for x in data03 if x % 2 == 0}
print(set01)




# -------------------------------------------------
# [참고] 제너레이터 컨프리핸션
# ( ) 를 사용하면 튜플이라 생각하지만 튜플은 컨프리핸션이 없다.
# 제너레이터 : 요소를 추출하면서 처리하고 저장을 하지는 않음
data03 = [1,2,3,4,5,4,2,6] # 마지막 결과형태인 set을 따라서 2,4,6이 한번씩만 출력이 됨
s01 = (x for x in data03 if x % 2 == 0)
print(s01)
print(list(s01))
print(list(s01)) # 두번째에는 나오지 않음
