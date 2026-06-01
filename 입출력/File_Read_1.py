f = open("/Users/mac/Desktop/python tutorial/새파일.txt", 'r',encoding ="UTF-8") #read 모드 활용
while True: #여러줄을 읽고 싶다면 반복문으로 다음줄을 읽어나가게됨
    line = f.readline()
    if not line : 
        break           #빈문자열이라면 break를 만나서 빠져나오게됨.
    print(line)
f.close()
