from urllib import request # request에 s가 붙어있지 않음

site = request.urlopen("http://www.google.com")
page = site.read()
#print(page) # html ~ html (태그) requests.content와 동일?..
            # 문자열을 byte로 취급하기 위해 문자열 앞에 b를 붙임
            # 정규식에 r 붙이는 것과 유사
#print(site.status)  # 200 -> 아무 문제 없이 web사이트에 접속했을 때
                    # 404 -> 페이지가 없을 경우 ..

header = site.getheaders()
#print(header)
for head in header:
    print(head[0], ">>", head[1])
# requests 패키지에서 뽑는 header 와 달리..
# 리스트와 그 안의 튜플이 있는 구조로 되어 있음