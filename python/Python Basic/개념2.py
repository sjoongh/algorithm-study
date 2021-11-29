"""
    print(2**3) # 2^3 = 8 
    print(6/3) # 실수형 몫 
    print(5//3) # 몫 1
    print(10//3) #몫 3
    print(5 % 3) #나머지 2

    print(5 > 4 > 3) #True

    print(abs(-5)) # abs -> 절대값
    print(pow(4, 2)) # pow -> 4^2 -> 제곱근
    print(max(5, 12))
    print(min(5, 12))
    print(round(3.14)) # round -> 반올림함수 -> 3
"""

from math import * # math라이브러리에 있는 모든 함수를 쓰겠다
print(floor(4.9)) # 내림함수 4
print(ceil(3.14)) #올림함수 4
print(sqrt(16)) #제곱근 4


from random import * # random 함수 
print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성(실수)
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성(실수)
print(int(random() * 10)) # 0.0 ~ 1.0 미만의 임의의 값 생성(정수)
print(int(random() * 10) + 1) # 1~ 10 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 정수

print(randrange(1, 46)) # 1 ~ 46 이하의 임의의값 생성
print(randint(1, 45)) # 양끝수를 모두 포함해서 출력해주는 랜덤함수

from random import *
date = randint(4, 28)
print("스터디모임"+str(date)+"이날")

#여러줄에 걸친 문자열
name3 = """
코딩
파이썬 ez
"""
print(name3)

#슬라이싱
jumin = "970123-123456"

print("연 : "+jumin[0:2]) # 배열 0부터 2직전까지 출력
print("생년월일 : "+jumin[:6]) # 처음부터 6직전까지 출력
print("뒤 7자리 : "+jumin[7:]) # 7부터 끝까지 출력
print("뒤 7자리 (뒤에부터) : "+jumin[-6:]) # 뒤에서부터 6자리 거꾸로 출력

#문자열 처리함수
# 원하는 문자를 찾는건 index와 find가 존재
python = "Python is Amazing"
print(python[0].isupper()) # 해당배열의 위치가 대문자인지 확인

index = python.index("n") # python 함수에서 n이 몇번째 위치에 있는지 알려줌
print(index)
index = python.index("n", index + 1) # 2번째 n을 찾음
print(index)
find = python.find("i") # 2번째 n을 찾음
print(find)
#find 는 find + 1이 안되는데 why?

#print(python.find("Java")) find는 원하는값이 없으면 -1반환, 프로그램은 계속 진행
#print(python.index("Java")) index는 오류발생, 프로그램이 끝나버림

print(python.count("n")) #python에서 n이 몇번 나오는지 count

#문자열 넣기
#방법 1
print("나는 %d살입니다" % 20)
print("나는 %s을 좋아해요" % "파이썬")
print("apple은 %c로 시작" % "A")
# %s는 정수 or 문자 상관없이 들어감
print("나는 %s살입니다" % 20)
print("나는 %s와 %s를 좋아해요" % ("파란", "빨간"))

#방법 2
print("나는 {}살입니다".format(20))
print("나는 {}와 {}을 좋아해요".format("파란", "빨간"))
print("나는 {1}와 {0}을 좋아해요".format("파란", "빨간"))
#중괄호는 연속된 값이 출력, 숫자를 넣으면 순서를 바꿀수있음

#방법 3
print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color = "빨간"))

age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")


#탈출문자

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")


# Quiz 
# http://부분은 제외 http://naver.com 으로 암호만들기
# 처음만나는 .이후 부분은 제외
# 남은글자중 처음 세자리 + 글자갯수 + 글자내 'e'개수 + "!"로 구성 (password)

url = "http://naver.com"
my_str = url.replace("http://", "") # 규칙1
my_str = my_str[:my_str.index(".")] # 규칙2
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e"))+ "!"
print("{0}의 비밀번호는 {1}입니다".format(url, password))

subway = ["name1", "name2", "name3"]
print(subway)

print(subway.index("name2")) # name2가 존재하는지 찾음 =

subway.append("name4") # name4를 추가함
print(subway)

subway.insert(1, "name5") #배열의 [1]번째 자리에 name5를 추가
print(subway)

# 뒤에서부터 하나씩 꺼냄
print(subway.pop())
print(subway)

#같은 이름의 사람이 몇명 있는지 확인
subway.append("name1")
print(subway)
print(subway.count("name1"))

#정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

# 순서 뒤집기
num_list.reverse()
print(num_list)

num_list.clear()
print(num_list)

# 리스트 확장
num_list = [5,2,4,3,1]
mix_list = ["조세호", 20, True]

num_list.extend(mix_list)
print(num_list)

#사전 자료형
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])
#위 코드는 오류뜸

#get을 이용했을때는 값이 없다면none  
print(cabinet.get(3))
print(cabinet.get(5))
print(cabinet.get(5, "사용가능"))

print(3 in cabinet)
print(5 in cabinet)

# 정수형이 아닌 문자 사전 자료형
cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 출력
print(cabinet.items())

# clear
cabinet.clear()
print(cabinet)

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스"), tuple은 첨삭은 안됨
# list는 첨삭 가능

#name = "sjh"
#age = 20;
#hobby = "코딩"
#print(name, age, hobby)

(name, age, hobby) = ("sjh", 20, "코딩")
print(name, age, hobby)

#집합 (set)
#중복안됨, 순서없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"유", "김", "양"}
python = set(["유", "박"])

#교집합 (jaava 와 pythone 모두 할 수 있는 사람)
print(java & python) # and로 출력
print(java,intersection(python)) # 교집합 코드 

#합집합 (java 할 수 있거나 python을 할 수 있는 사람)
print(java | python) # or
print(java.union(python))

#차집합 (java 할 수 있지만 python은 할 줄 모르는 사람)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김")
print(python)

# java를 잊어버림
java.remove("김")
print(java)

#자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))


from random import *
users = range(1, 21) # 1부터 20까지 숫자 생성
# print(type(users))
users = list(users) # list타입을 사용하기 위해 range에서 바꿈
# print(type(users))
shuffle(users)

pick = sample(users, 4) # 4명중에서 1명은 치킨, 3명은 커피
print("당첨자")
print("치킨당첨자 : {0}".format(pick[0]))
print("커피당첨자 : {0}".format(pick[1:]))
print("축하합니다")




































