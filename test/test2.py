f = open("dream.txt", 'r', encoding='utf-8')
cnt = 0
while True:
    line = f.readline()
    if not line: break
    print(str(cnt)+"---"+line, end='')
    cnt+=1
f.close()