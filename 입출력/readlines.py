f = open("/Users/mac/Desktop/python tutorial/새파일.txt", 'r',encoding ="UTF-8") #read 모드 활용
lines = f.readlines()
for line in lines:

    line = line.strip() # strip() 함수를 통해 /n 줄바꿈 문자를 제거한다.
    print(line)
f.close()