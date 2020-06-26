"""
 urllib.parse.urljoin() : 상대경로를 절대경로로 변화하는 함수
"""
#from urllib import parse
from urllib.parse import urljoin
#함수 하나만 가져오는 경우

baseurl = 'http://www.example.com/html/a.html'

print(urljoin(baseurl, 'b.html'))
print(urljoin(baseurl, 'sub/c.html'))
print(urljoin(baseurl, '/sub/c.html')) #페이지의 루트부분부터 시작을 해줌
print(urljoin(baseurl, '../sub/c.html')) #부모로 올라가서..
print(urljoin(baseurl, 'http://www.daum.net')) #아예 통째로 변경됨