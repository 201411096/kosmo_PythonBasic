msg = '밥먹자'                   # 문자열
li = ['a','b','c']              # 리스트
tpl = ('ㄱ','ㄴ','ㄷ')           # 튜플
di = dict(k=5, j=6, i=7)        # 딕셔너리
    # ㄴ di = {k-5, j=6, i=7} 과 동일한 코드

#----------------------------------------
# (1) unpacking : 각 요소를 분해
c1, c2, c3 = di    # 문자열 뿐만 아니라 리스트, 튜플, 딕셔너리 전부 가능함
print(c1, c2, c3)

#----------------------------------------
# (2) 리스트의 요소가 튜플인 경우
alist = [ (1,2), (3,4), (5,6) ]
for a in alist:
    print(a)
for (a, b) in alist:
    print("# (2) 리스트의 요소가 튜플인 경우 확인", a, b)
    
#----------------------------------------
# (3) enumerate() 함수
user_list = ['개발자', '코더', '전문가', '분석가']
#user_list = {'개발자', '코더', '전문가', '분석가'}
for user in user_list:
    print("# (3) enumerate() 함수 사용 전 확인", user)

# index가 붙으면서 tuple로 받아옴
for user in enumerate(user_list):
    print("# (3) enumerate() 함수 사용 후 확인", user)

#----------------------------------------
# (4) zip() : 여러 시퀀스를 순회하는 함수
days = ['월', '화', '수']
doit = ['잠자기', '놀기', '밥먹기', '공부']

print("# (4) zip() 함수 사용 후 확인", zip(days, doit))
print("# (4) zip() 함수 사용 후 tuple로 변환 후 확인", tuple(zip(days, doit)))
print("# (4) zip() 함수 사용 후 list로 변환 후 확인", list(zip(days, doit))) # 짝꿍을 지어서 묶어줌
print("# (4) zip() 함수 사용 후 dict로 변환 후 확인", dict(zip(days, doit))) # 짝꿍을 지어서 묶어줌

mon=[6,7,8]
print(list(zip(days, doit, mon)))
# print(dict(zip(days, doit, mon))) # dictionary는 3개씩 묶을 수는 없음