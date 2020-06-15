"""
import datetime
today = datetime.date.today();
print('today is ', today)
"""
from datetime import date
today = date.today()
print('오늘은 ', today)

#년, 월, 일
print('년도 :', today.year)
print('년도 :', today.month)
print('년도 :', today.day)

#날짜계산
from datetime import timedelta
print('어제 : ', today+timedelta(days=-1))
#7일전
print('7일전 :', today+timedelta(weeks=-1))
#10일 후
print('10일전 :', today+timedelta(days=+10))

#날짜와 문자열 변환
#날짜(년월일)와 시분초까지 같이 가져옴
from datetime import datetime
today=datetime.today()
print(today)
print(today.strftime('%Y/%m/%d %H:%M'))

nalja = '2020-08-08 12:12:35'
mydate = datetime.strptime(nalja, '%Y-%m-%d %H:%M:%S')