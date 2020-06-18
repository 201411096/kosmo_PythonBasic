'''
    # compile
     - 동일한 정규표현식을 매번 다시 쓰기 번거로움을 해결
     - compile로 해당표현식을 re.RegexObject 객체로 저장하여 사용가능
'''

import re


#----------------------------------------
webs = ['http://www.test.co.kr',
        'https://www.test1.com',
        'http://www.test.com',
        'ftp://www.test.com',       # 잘못된 형식
        'http:://www.test.com',     # 잘못된 형식
       'htp://www.test.com',        # 잘못된 형식
       'http://www.google.com',
       'https://www.homepage.com.'] # 잘못된 형식

# 올바른 웹형식 : http 혹은 https 로 시작, :// 이 따라오고, 마지막은 문자로 끝남
# re.compile을 사용하여 정규 표현식(위 예에서는 ab*)을 컴파일한다.
web_reg = re.compile('https?://[\w.]+[\w]+$')
# s가 없거나 있을 수 있음 => s?
# \w+$ => 문자로 끝남
result = list(map(lambda w:web_reg.search(w) != None, webs))   # map(함수, 리스트)
# 매칭이 될 경우 True 매칭이 안되면 False
print(result)