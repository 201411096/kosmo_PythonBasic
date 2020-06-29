"""
    HTML 내부에 있는 링크를 추출하는 함수
        - CSS 파일과 a 링크 연결된 모든 파일을 가져오기
"""

from bs4 import BeautifulSoup
from urllib import parse
from urllib import request

def enum_links(html,base):
    #-------------------------------------
    result = []
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select('a[href]')  # href속성을 갖고있는 a태그들을 찾음
    # print(links)
    # print('-'*50)                 
    for a in links:
        href = a.attrs['href']      # 상대경로와 절대경로가 섞여있음
       #print(href)
        url = parse.urljoin(base, href)
        result.append(url)
        # index.html -> https://docs.python.org/3.7/library/index.html
        # ../start.html -> https://docs.python.org/3.7/start.html
        # http://py.com -> http://py.com
    return result

if __name__ == '__main__':
    url = 'https://docs.python.org/3.7/library/'
    response = request.urlopen(url)   # urllib.request.urlopen() : BeautifulSoup을 통해 html 파서할(데이타를 가져올) 대상
    result = enum_links(response, url)
    print(result)