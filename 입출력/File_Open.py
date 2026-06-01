f = open("/Users/mac/Desktop/python tutorial/새파일.txt", 'w',encoding ="UTF-8") #read 모드 활용
for i in range(1,11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
