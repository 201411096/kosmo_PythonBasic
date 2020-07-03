f = open("sample.txt", 'r')
sum = 0
cnt = 0
while True:
    line = f.readline()
    if not line: break
    sum+=int(line)
    cnt+=1
f.close()
fw = open("result.txt", "w")
fw.write("total : " + str(sum) +"\n")
fw.write("avg : " + str(sum/cnt))
fw.close()