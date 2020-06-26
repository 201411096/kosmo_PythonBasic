'''
    http://www.data.go.kr
            - 회원가입필수
            - 일반인증키 요청 ( 바로 받을 수 있고 자료요청시 바로 승인됨 )

    >  관광자원통계서비스  >  상세기능 > 유료관광지방문객수조회
    : 전국의 주요 유로관광지 방문객수를 조회하기 위한 서비스로서
    기간,지역, 관광지별 외국인 방문객수와 내국인 방문객수를 조회한다.

    의미있는 데이타를 추출하여 출력한다

'''


from urllib import request
from urllib import parse
from ast import literal_eval # str을 dictionary로 변경
import json
import requests

access_key = '발급받은 키 값'


url = 'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList'
queryParams = '?_type=json'
queryParams += '&serviceKey=' + access_key
queryParams += '&YM=' + '201201'
queryParams += '&SIDO=' + parse.quote('부산광역시')
queryParams += '&GUNGU=' + parse.quote('해운대구')
queryParams += '&RES_NM=' + parse.quote('부산시립미술관')
# queryParams += '&SIDO=' + parse.quote('서울특별시')
# queryParams += '&GUNGU=' + parse.quote('종로구')
# queryParams += '&RES_NM=' + parse.quote('경복궁')

req = request.Request(url + queryParams) # request 객체
response = request.urlopen(req)
returndata = response.read().decode('utf-8')

print(returndata)
print(type(returndata))
returndata = json.loads(returndata)
#returndata = literal_eval(returndata)
#str을 dictionary 로 변경

#내국인 관광객 수
print(returndata["response"]["body"]['items']['item']['csNatCnt'])
#외국인 관광객 수
print(returndata["response"]["body"]['items']['item']['csForCnt'])