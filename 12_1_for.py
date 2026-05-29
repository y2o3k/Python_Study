#학생들의 점수를 합불 판정
marks = [90, 25, 67, 45, 80] # 학생들의 시험점수 리스트
number = 0 # 순차적으로 학생에게 붙여줄 번호 = 학생들의 점수를 뽑아냄.
for mark in marks:
    number = number + 1 
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)