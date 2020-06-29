"""
    파이썬은 파일하나를 모듈로 취급한다면 다른 파일의 함수를 복사하지 않고 바로 호출한다.

    [주의] import Ex07_alldown1 코드부터 에러발생하지만 실행은 됨

"""


from bs4 import BeautifulSoup
from urllib.parse import *
from urllib.request import *
import os, time, re

# 에러 발생해도 실행은됨
import Ex07_alldown1
import Ex07_alldown2


# 이미 처리한 파일인지 확인하기 위한 변수
proc_files = {} # set or dictionary
                # ( ) : tuple
                # [ ] : list

# HTML을 분석하고 다운받는 함수
def analyze_html(url, root_url):
    # ------------------------------------------------------
    savepath = Ex07_alldown2.download_file(url)
    if savepath is None: return # 다운로드가 실패했을 경우
    # 이미 처리된 파일이라면 proc_files에 있기에 실행하지 않음
    if savepath in proc_files : return
    proc_files[savepath] = True   # {'https://docs.python.org/3.5/library/', True}
    # 링크 추출
    f = open(savepath, "r", encoding="utf-8")
    html = f.read()
    links = Ex07_alldown1.enum_links(html, url)
    for link_url in links:
        if link_url.find(root_url) != 0: continue   # 찾으면 맨 첫번째값을 반환하기 때문에...?
        if re.search('.html$', link_url):
            analyze_html(link_url, root_url)    #재귀함수
            continue
        Ex07_alldown2.download_file(link_url)

if __name__ == "__main__":
    # URL에 있는 모든 것 다운받기
    url = "https://docs.python.org/3.5/library/"
    analyze_html(url, url)
    # 첫번째 매개변수는 base경로?