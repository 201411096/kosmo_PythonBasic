"""
    파일을 다운받고 저장하는 함수

     [참고] 파이썬 정규식 표현 : https://wikidocs.net/4308
"""
from bs4 import BeautifulSoup
from urllib import parse
from urllib import request
import os, time, re  # re : 정규식

def download_file(url):
    p = parse.urlparse(url)
    print('1-', p)
    savepath = "./"+p.netloc+p.path
    print('2-', savepath)
    # 마지막에 '/' 끝나면 index.html이 생략했다고 고려하여 index.html을 붙임
    if re.search('/$', savepath):      # savepath가 '/'로 끝날경우
        savepath += 'index.html'
        print('3-', savepath)
    
    # 로컬 폴더에 파일이 존재하는지
    if os.path.exists(savepath): return savepath
    
    # 다운받을 폴더가 없으면 생성
    savedir = os.path.dirname(savepath)
    if not os.path.exists(savedir):
        os.makedirs(savedir)
            # mkdir <-> makedirs
            # mkdir : ..
            # makedirs : 하위 폴더까지 생성을 함
    # 파일 다운받기
    try:
        print('download : ', url)
        request.urlretrieve(url, savepath)
        # urlretrieve(args1, args2)
        #       args1 : 다운로드 받을 위치
        #       args2 : 다운로드 받은 후 파일 이름
        # retrieve : 검색하다 되찾아오다
        time.sleep(2)
        return savepath
    except:
        print('fail download ...', url)
        return None

if __name__ == '__main__':
    url = 'https://docs.python.org/3.6/library/'
    #url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%E3%85%81%E3%84%B4%E3%85%87%E3%84%B9'
    # 결과가 생각한 것처럼 안나옴
    result = download_file(url)
    print(result)


"""
urlparse
    ㄴ scheme://netloc/path;parameters?query#fragment
    ㄴ scheme : URL 스킴 지정자
    ㄴ netloc : 네트워크 위치 부분
    ㄴ path : 계층적 경로
    ㄴ params : 마지막 경로 요소의 파라미터
    ㄴ query : 쿼리 구성 요소
        ㄴ 쿼리스트링 부분
    ㄴ fragment : 프래그먼트 식별자
"""
