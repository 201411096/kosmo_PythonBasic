from pathlib import Path

# ------------------------------------------------
# 1. 경로의 상태보기
# print(Path.cwd())   #리눅스의 pwd
# print(Path.home())  #리눅스의 홈디렉토리 경로 확인
# ----------------------------------------------------
# 2. 경로(파일) 생성시간 알아보기
# p = Path('Ex03_createPath.py')
# print(p.stat().st_ctime) # 1970.1.1 0시 0분 0초
#
# from datetime import datetime
# z = datetime.fromtimestamp(p.stat().st_ctime)
# print("datetime의 fromtimestamp 사용 이후", z)
# ------------------------------------------------
# 3. 디렉토리 생성
# p1 = Path('imsi')
# p1.mkdir(exist_ok=True)

# p2 = Path('imsi')
# p2.mkdir(exist_ok=True) #존재한다면 덮어쓰기

# p3 = Path('temp2/imsi2/test2')
# p3.mkdir(exist_ok=True, parents=True)
# ------------------------------------------------
# 4. 파일 생성
# f = open('imsi/1.txt', 'w', encoding='utf-8') #write 모드로 여는 경우 -> 파일이 존재하지 않을 경우 생성을 해줌
# f.write('')
# f.close()
#
# f2 = Path('imsi/2.txt')
# f2.touch()
# ------------------------------------------------
# 5. 경로 제거
#f = Path('temp2/imsi2/test2')
f = Path('imsi')
f.rmdir()   # 비어있는 폴더가 아니라서 지워지지 않음 : OSError: [WinError 145]