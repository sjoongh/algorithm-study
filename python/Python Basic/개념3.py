weather = input("오늘 날씨?")
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크")
else:
    print("준비물 x")

temp = int(input("기온은 어때요?")) #input은 항상 문자열로 값을 받기 때문에
#int형으로 바꿔줘야함
if 30 <= temp:
    print("더워요")
elif 10 <= temp and temp < 30:
    print("좋아요")
elif 0 <= temp and temp < 10:
    print("추워요")
else :
    print("개추")

for waiting_no in [0, 1, 2, 3, 4,]:
# for wating_no in range(5) 라고 해도 가능
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["num1", "num2", "num3", "num4"]
for customer in starbucks:
    print("{0}, coffee ready".format(customer))

# while

# customer = "토르"
# index = 5
# while index >= 1:
#    print("{0}, coffee is ready. {1}is left".format(customer, index))
#    index -= 1
#    if index == 0:
#        print("coffee is sold out")

# customer = "lron man"
# index = 1
# while True:
#    print("{0}, coffee is ready. 호출 {1}회 ".format(customer,index))
#    index += 1

# customer = "토르"
# person = "Unknown"

# while person != customer:
#    print("{0}, coffee ready".format(customer))
#    person=input("name?")

absent = [2, 5]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in absent:
        print("today class is over. {0} come to me".format(student))
        break
print("{0}, read a book".format(student))

# 출석번호가 1 2 3 4, 앞에 100을 붙이기로함
students = [1,2,3,4,5]
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)

# 지하철 탑승 승객
from random import *
cnt = 0
for i in range(1, 51): # 1 ~ 50이라는 수(승객)
    time = randrange(5, 51) # 5분 ~50분 소요시간
    if 5 <= time <= 15: # 5분 ~15분 이내 손님, 탑승 승객수 증가 처리
        print("[0] {0}번째 손님 (소요시간 : {1}분".format(i, time))
        cnt += 1
    else: # 매칭 실패
            print("[ ] {0}번째 손님 (소요시간 : {1}분".format(i, time))
print("총 탑승 승객 : {0} 분".format(cnt))
