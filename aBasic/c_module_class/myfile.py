#myfile.py

# (1) 전체 모듈 사용시
"""
import mymodule as mm

print('오늘의 날씨 :', mm.get_weather())
print('오늘의 요일 :', mm.get_date())
"""
# (2) 모듈을 부분적으로 사용시 + 패키지에서 끌어올 때 
#from mypackage.mymodule import get_weather, get_date
#from mypackage.mymodule import *
#print('오늘의 날씨 :', get_weather())
#print('오늘의 요일 :', get_date())

# (3) 모듈을 부분적으로 사용시 + 패키지에서 끌어오면서 별칭도 줌
# from mypackage import mymodule as mm
# print('오늘의 날씨 :', mm.get_weather())
# print('오늘의 요일 :', mm.get_date())