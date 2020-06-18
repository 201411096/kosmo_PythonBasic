"""
경로 이동은  Path 모듈로 안되어 os 모듈이 필요하다
"""
import shutil
from pathlib import Path
#shutil.rmtree('imsi') # 하위 디렉토리에 다른 파일이 있는 경우에도 지워줌

#shutil.copy('Ex00.txt', Path('temp2/imsi2/2copy.txt'))  # shutil.copy(복사할파일, 복사할 위치와 파일이름)

#shutil.copytree('temp2', '../copytemp')
shutil.rmtree('../copytemp')