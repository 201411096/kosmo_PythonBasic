f = open("dream.txt", 'r', encoding='utf-8')
linecnt = 0
wordcnt = 0
charcnt = 0
while True:
    line = f.readline()
    if not line: break
    charcnt+=len(line)
    wordcnt+=len(line.split())
    linecnt+=1

f.close()
print("총 글자의 수", charcnt)
print("총 단어의 수", wordcnt)
print("총 줄의 수", linecnt)