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
        time.sleep(2)
        return savepath
    except:
        print('fail download ...', url)
        return None

if __name__ == '__main__':
    url = 'https://docs.python.org/3.6/library/'
    result = download_file(url)
    print(result)


"""
urlparse
    ㄴ scheme 
    ㄴ netloc 
    ㄴ path 
    ㄴ params 
    ㄴ query 
    ㄴ fragment 
"""
