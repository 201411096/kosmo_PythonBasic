"""
http://www.seoul.go.kr > 청사안내 > 자치구
https://www.seoul.go.kr/seoul/autonomy.do

BeautifulSoup  : 파서를 이용해서 html 의 요소를 추출하게 해주는 모듈
        - 단점은 개행문자를 고려해야 한다
Tag : 태그
NavigableString : 원래는 tag 사이의 문자열

#  xpath를 사용하면 개행문자를 고려하지 않아도 된단다
#  https://developer.mozilla.org/ko/docs/XPath
"""

from urllib import request
from bs4 import BeautifulSoup

html = 'http://www.seoul.go.kr/seoul/autonomy.do'
site = request.urlopen(html)
site1=site.read()

soup = BeautifulSoup(site1,"html.parser")

# 아래 리스트에 각 구청의 상세 정보를 저장하고 출력하기
구청이름=[]
구청주소=[]
구청전화번호=[]
구청홈페이지=[]
구청홈페이지=[]
