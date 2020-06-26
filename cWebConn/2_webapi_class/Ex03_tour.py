from urllib import request
from urllib import parse
import datetime
import json
import math

"""  관광지 입장객 정보 획득을 위한 파라메터 설정하여 결과를 얻어오는 함수
       - 년도, 시도, 구군, 페이지번호, 한페이지결과수를 지정 """
def getTourPointVistor(yyyymm, sido, gungu, nPgaenum, nItems):
    # -----------------------------------------------------------
    # 여기에 코드
    access_key = '키값입력하세요'

    url = 'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList'

    queryParams = '?_type=json'
    queryParams += '&serviceKey=' + access_key
    queryParams += '&YM=' + yyyymm
    queryParams += '&SIDO=' + parse.quote(sido)         # 웹에서 한글텍스트를 % 인코딩으로 변환
    queryParams += '&GUNGU=' + parse.quote(gungu)
    queryParams += '&RES_NM=&pageNo=' + str(nPgaenum)   # RES_NM 값 없다고 제거하면 안된다
    queryParams += '&numOfRows=' + str(nItems)




''' 각 항목을 JSON 구조로 변경하고 추가하는 함수'''
def getTourPointData(item, yyyymm, jsonResult):
    addrCd = 0 if 'addrCd' not in item.keys() else item['addrCd']
    gungu = 0 if 'gungu' not in item.keys() else item['gungu']
    sido  = 0 if 'sido' not in item.keys() else item['sido']
    resNm = 0 if 'resNm' not in item.keys() else item['resNm']
    rnum = 0 if 'rnum' not in item.keys() else item['rnum']
    ForNum = 0 if 'ForNum' not in item.keys() else item['ForNum']
    NatNum = 0 if 'NatNum' not in item.keys() else item['NatNum']

    jsonResult.append({'yyyymm' : yyyymm,
                       'addrCd' : addrCd,          # 지역코드 ( 우편번호와 일치한다고 하는데 )
                       'sido': sido,                # 시도
                       'gungo' : gungu,             # 구군
                       'resNm' : resNm,             # 관광지명
                       'rnum' : rnum,               # 관광지에 고유하게 부여된 코드값
                       'ForNum' : ForNum,           # 외국인수
                       'NatNum' : NatNum})          # 내국인수


''' 추출할 변수 지정하고 필요한 함수 호출하여 결과 받는 메인 함수'''
def main():
    jsonResult = []    # 결과 저장 변수

    # 검색할 변수값 지정
    sido = '서울특별시'      # 시도
    gungu = ''               # 구군
    nPagenum = 1             # 페이지번호
    nTotal = 0
    nItems = 100              # 한 페이지의 레코드 수? 100개가 넘으면 다음 페이지로 넘어가도록
                              # sido가 경기도면 100개가 넘어가 페이지 처리가 필요하단다
    nStartYear = 2015         # 추출할 년도의 시작년도
    nEndYear = 2017           # 추출할 년도의 종료년도

    #-----------------------------------------------------------
    # 여기에 코딩하기
    for year in range(nStartYear, nEndYear): #2015 ~ 2016
        for month in range(1, 13):
            # {1:0>2} => 2자리 공간을 만들고 빈 공간은 0으로 채우기
            yyyymm = "{0}{1:0>2}".format(str(year), str(month))
            nPagenum = 1
            while True:
                jsonData = getTourPointVistor(yyyymm, sido, gungu, nPagenum, nItems)
                if jsonData['response']['header']['resultMsg'] == 'OK':
                    nTotal = jsonData['response']['body']['totalCount']
                    if nTotal == 0:break

                    for item in jsonData['response']['body']['items']['item']:
                        getTourPointData(item, yyyymm, jsonResult)
                    nPage = math.ceil(nTotal/100); # 올림 nTotal=80, nPage=1 | nTotal=180, nPage=2
                    if nPage == nPagenum: break
                    nPagenum += 1
                else : break
            with open('./data/%s_관광지입장정보_%d_%d.json'%(sido, nStartYear, nEndYear-1), "w", encoding='utf-8') as f:
                # 속성 찾아보기
                saveToJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
                f.write(saveToJson)




    print('%s_관광지입장정보_%d_%d.json로 저장되었읍니다.'%(sido, nStartYear, nEndYear-1))


''' 프로그램 시작점 '''
if __name__ == '__main__':
    main()

