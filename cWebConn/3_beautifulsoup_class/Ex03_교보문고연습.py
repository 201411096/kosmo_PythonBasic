'''
 [과제] 교보문고에서 파이썬 책 검색하여
    - csv 파일로 저장
    - mysql 테이블에 저장
'''


from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

# 교보문고 > '파이썬' 검색 > 국내도서
html = urlopen("http://www.kyobobook.co.kr/search/SearchKorbookMain.jsp?vPstrCategory=KOR&vPstrKeyWord=python&vPplace=top")
#html = urlopen('https://search.kyobobook.co.kr/web/search?vPstrKeyWord=%25ED%258C%258C%25EC%259D%25B4%25EC%258D%25AC&orderClick=LAG')
# 책 제목 뽑아오기
soup = BeautifulSoup(html, 'html.parser')
bookNameList = soup.select('div.title > a > strong')
#bookNameTextList = []
for bookName in bookNameList:
    print(bookName.text)
#    bookNameTextList.append(bookName.text)
print("총 책의 권수", len(bookNameList))

# 이미지 뽑아오기
# imagepath = 'data/'
# bookImageList = soup.select('div.cover > a > img')  #find_all ?...
# for idx, bookImage in enumerate(bookImageList):
#     print(bookImage.attrs['src'])
#     urlretrieve(bookImage.attrs['src'], imagepath+str(idx)+'.jpg')

#이미지 뽑아오기_2 쿡북 문제 생김
imagepath = 'data/'
bookImageList = soup.select('div.cover > a > img')  #find_all ?...
for idx, bookImage in enumerate(bookImageList):
    print(bookImage.attrs['src'])
    bookName = bookImage.attrs['alt'].replace('/', '')
    bookName = bookName.replace('?', '')
    urlretrieve(bookImage.attrs['src'], imagepath+bookName+'.jpg')
