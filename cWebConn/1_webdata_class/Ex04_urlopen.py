
# urlretrieve(): 파일로 바로 저장
# urlopen(): 파일로 바로 저장하기 않고 메모리에 로딩을 한다.

""" [참고] 파일저장 기본방식
    f = open('a.txt','w')
    f.write("테스트 내용")
    f.close()

    위의 과정을 with 문으로 간략하게 close 필요없음
    with open("a.txt","w") as f:
        f.write("테스트 내용")
"""
from urllib import request
url = "https://t1.daumcdn.net/daumtop_chanel/op/20170315064553027.png"
imgName = "data/daum.png"

site = request.urlopen(url)
downImg = site.read()   #downImg는 특정 객체를 가리키고 있음
                        #retrieve는 메모리에 올리지 않고 바로 저장했었음
                        #urlopen은 메모리에 올렸다가 다시 저장
                        #특별한 작업없이 이미지를 다운로드 받는 목적이라면 urlretrieve를 사용하는 것이 맞음
#wb 는 write + binary (이미지 파일이기때문에..)
with open(imgName, 'wb') as f:
    f.write(downImg)


