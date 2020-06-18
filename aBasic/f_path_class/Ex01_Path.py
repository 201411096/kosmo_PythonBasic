"""
 - import pathlib 만 선언하면
        Path클래스 사용시 pathlib.Path라고 명시해야 한다. 
"""
from pathlib import Path
# from pathlib import Path as p => 이런식으로 별칭 가능(대부분 관용화된 별칭을 사용함)
# import pathlib

# (1) 해당 경로와 하위 목록들 확인

p = Path('C:\Windows')
# p = Path('.')# 현재 경로
# p = Path('..')
print(p)
print("resolve 함수를 이용한 상대경로 <-> 절대경로 변환 =>>", p.resolve())# 절대 경로로 보여줌

# 하위디렉토리 찾기_01
# test = []
# for x in p.iterdir():       # iterdir()
#     if x.is_dir():          # is_dir() => directory인지 확인
#         test.append(x)
# 하위디렉토리 찾기_02 (리스트 컴프리헨션 사용)
test = [x for x in p.iterdir() if x.is_dir()]   # list comprehension 사용
print("하위 디렉토리 목록 확인 =>>", test)
# 하위 파일 찾기
test = [x for x in p.iterdir() if x.is_file()]   # list comprehension 사용
print("하위 파일 목록 확인 =>>", test)

#a = list(p.glob('./a_datatype_class/*.py'))
a = list(p.glob('**/a_datatype_class/*.py'))# **/ 하위자손들 중에서 확인
print(a)