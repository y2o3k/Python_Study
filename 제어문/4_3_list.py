#리스트 데이터 타입 공부 

students = ["egoing","sori","maru"] 
grades = [2,1,4] #2학년 ,1학년 ,4학년이 있다고 가정. 
# sori 라는 단어를 가지고 오고 싶을 경우 
print("students[1]", students[1])
print("len(students)", len(students)) #리스트에 3개의 값이 들어가 있음.

print(min(grades))
print(max(grades))
print(sum(grades))

#통계와 관련된 함수 호출 
import statistics
print("statics.mean(grades)", statistics.mean(grades)) #평균값 산출

#랜덤으로 뽑기
import random
print("random.choice(students)", random.choice(students)) #랜덤으로 학생 이름 하나 뽑기