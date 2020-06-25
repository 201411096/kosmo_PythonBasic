import os
from datetime import *
from random import *
if not os.path.isdir('logtemp'):
    print('디렉토리 생성됨')
    os.mkdir('logtemp')

if not os.path.isfile('logtemp/temp_log.txt'):
    print('파일이 생성됨')
    f = open("logtemp/temp_log.txt", 'w+')
    for num in range(0, 10):
        f.write(datetime.today().strftime("%Y/%m/%d %H:%M:%S"))
        f.write(str(randint(1, 100)))
        f.write('\n')
    f.close()
else:
    print('파일이 존재함')
    f = open("logtemp/temp_log.txt", 'a+')
    for num in range(0, 10):
        f.write(datetime.today().strftime("%Y/%m/%d %H:%M:%S"))
        f.write(str(randint(1, 100)))
        f.write('\n')
    f.close()