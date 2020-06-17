# Ex02_csv.py

import csv
# 1. 리스트의 데이터를 csv로 저장하기
data = [ [1, '감', '책임'], [2, '주', '연구원'] ]
with open('./data.imsi.csv', 'wt', encoding='utf-8') as f:
    cout = csv.writer(f)
    cout.writerows(data)

# 2. csv 파일을 읽어서 리스트 변수에 저장하기
data = []
with open('./data.imsi.csv', 'r', encoding='utf-8') as f:
    cin = csv.reader(f)
    data = [row for row in cin if row]  # row값이 있을 경우에만 리스트가 추가됨 # 이 문장이 없으면 비어있는 리스트가 들어가있음 
print(data)