from bs4 import BeautifulSoup

html = """
    <html>
        <body>
            <ul>
                <li><a href='http://www.naver.com'>네이브</a></li>
                <li><a href='http://www.daum.net'>다아음</a></li>
            </ul>
        </body>
    </html>
"""

# 리스트의 내용과 해당 경로를 추출하기
soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all('a')
for link in links:
    print(link.attrs['href'])   #태그의 속성값을 가져옴