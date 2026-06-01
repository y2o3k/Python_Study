f = open("/Users/mac/Desktop/python tutorial/새파일.txt", 'a') #read 모드 활용
for i in range(11,20): 
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()