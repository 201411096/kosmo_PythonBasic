"""
    # [참고] 파이썬 정규식 표현
            - https://docs.python.org/3/library/re.html
            - https://wikidocs.net/4308 > re

    # raw string
        - 문자열 앞에 r이 붙으면 해당 문자열이 구성된 그대로 문자열로 변환

    # 패턴과 소스를 비교하는 메소드
    - match() : 패턴의 일치여부 확인
                search와 유사하나, 주어진 문자열의 시작부터 비교하여 패턴이 있는지 확인
                시작부터 해당 패턴이 존재하지 않다면 None 반환
    - findall() : 일치하는 모든 문자열 리스트 반환
                search가 최초로 매칭되는 패턴만 반환한다면, findall은 매칭되는 전체의 패턴을 반환
                매칭되는 모든 결과를 리스트 형태로 반환
    - search() : 첫번째 일치하는 객체 반환

    - split() : 패턴에 맞게 소스를 분리한 후 문자열 조각의 리스트 반환
    - sub() : 주어진 문자열에서 일치하는 모든 패턴을 replace
            그 결과를 문자열로 다시 반환함
            count가 0인 경우는 전체를, 1이상이면 해당 숫자만큼 치환 됨

"""

import re

#re : 파이썬의 정규 표현식을 지원하는 모듈 (regular expression의 약어)

# r : raw string
a = 'abcdef\n'      # escapce 문자열
b = r'abcdef\n'     # r을 붙이면 '', ""안에 있는 모든것을 문자로 취급함
print(a)
print(b)




# match
msg = 'We are happy. You are happy. Happy2019 2020'

result = re.match('^We', msg)
if result:
    print(result.group())
result = re.match('.*happy', msg)
if result:
    print(result.group())
result = re.match('.Happy', msg)
if result:
    print(result.group())
print('='*50)
# search
result = re.search('.Happy', msg)
if result:
    print(result.group())
print('='*50)
# split
result = re.split('a', msg)
print(result)
print('='*50)
# sub
result = re.sub('a', '@', msg)
print(result)