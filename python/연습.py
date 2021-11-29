# year, month, day, hour, minute, second = input().split()
# print(year, month, day, sep='-', end='T')
# print(hour, minute, second, sep =':')

# is, is not은 객체(object)를 비교함
# 1 == 1.0 -> True
# 1 is 1.0 -> False
# 1 is not 1.0 -> True-

# 10 == 10 and 10 != 5
# 10 > 5 or 10 < 3
# not 1 is 1.0

# num1, num2, num3, num4 = map(int, input().split())
# print(num1 >= 90 and num2 > 80 and num3 > 85 and num4 >= 80)

# empty list
# a = []
# b = list()

# range(연속된 숫자 생성)
# a = list(range(10)) -> 0~9까지 들어있는 리스트
# 리스트 = list(range(시작, 끝))
# b = list(range(5, 12))
# 리스트 = list(range(시작, 끝, 증가폭))
# c = list(range(-4, 10, 2))
# d = list(range(10, 0, -1))

# 튜플 : 읽기전용 리스트(변경, 추가 삭제불가능), 괄호로 묶어주면 튜플이 됨
# a = (38, 21, 53, 62, 19)
# a = tuple(range(10))

# a = [1, 2, 3] # 리스트 패킹
# b = (1, 2, 3) # 튜플 패킹
# c = 1, 2, 3 # 튜플 패킹

# 특정 값이 있는지 확인하기, 튜플, range, 문자열도 확인가능
# 10 in a -> False
# 3 in a -> True
# 10 not in a -> True
# 3 not in a -> False


# 시퀀스(연속적으로 이어진 자료형) 객체는 + 연산자를 이용해 서로 연결할수있다
# range는 기호 연산자로 연결할수없음, 튜플or 리스트로 바꿔줘야함
# range(0, 10) + range(10, 20) -> list(range(0, 10)) + list(range(10, 20))

# 시퀀스 객체 반복, 0또는 음수를 곱하면 빈객체, 실수는 곱할수없음
# [0, 10, 20, 30] * 3

# 리스트와 튜플의 요소 개수 구하기
# a = [0, 1, 2, 3, 4]
# len(a) -> 5
# len(range(0, 10, 2) -> 5

# 문자열의 길이
# hello = 'Hello, world!'
# len(hello) -> 13

# 인덱스로 리스트의 요소에 접근
# a = [38, 21, 53, 62, 19]
# a[-3] -> 뒤에서 3번째 요소 53출력
# a[len(a) - 1] -> 마지막요소 출력
# del a[2] -> 세번째요소 삭제

# 슬라이스
# a = [0, 1, 2, 3, 4, 5]
# print(a[0:3]) -> 0, 1, 2
# a[2:8:3] -> 인덱스 2부터 3씩 증가시키면서 인덱스 7까지 가져옴
# 시퀀스객체[시작인덱스:끝인덱스:증가폭]
# a[:7:2] -> 시퀀스객체[:끝인덱스:증가폭]
# 시퀀스객체[시작인덱스::증가폭] -> a[7::2] 인덱스 7부터 2씩 증가시키면서 마지막요소까지 출력
# 시퀀스객체[::증가폭] -> a[::2] 리스트 전체에서 0부터 2씩 증가시켜 출력
# 리스트전체 -> a[:], a[::]

# 역순출력 -> a[5:1:-1] 시작인덱스가 끝인덱스보다 커야함

# 슬라이스에 요소 할당
# a[2:5] = ['a', 'b', 'c']

# 딕셔너리 사용하기, 특정주제에 연관된 값을 저장할때 사용
# 딕셔너리 = {키1: 값1, 키2: 값2}
# lux = {'health': 490, 'mana' : 334}
# 빈 딕셔너리 x = {}

# lux = {'health': 490, 'mana': 334, 'melee': 550}
# lux['mana'] = 1184
# lux['health'] = 2037
# mana와 health의 값이 바뀜

# x = input().split()
# y = map(float,input().split())
# lux =dict(zip(x,y)) -> zip함수를 통해 x와 y를 묶어줌
# print(lux)

# if x == 10:
#    pass # TODO : x가 10일 때 처리가 필요함 -> TODO(관습)로 나중에 처리할일 주석처리
# pass 는 아무일도 발생하지 않고 넘어감

# if 조건문에서는 =(할당 연산자)를 사용할 수 없음 >, is, not, != 등등은 가능
# if 조건문에서는 & 사용이 안되는듯??, 주로 논리연산자 사용 and,or,not

# for 변수 in range(횟수): -> for i in range(100):
#      반복할 코드 ->             print('Hello world!')
# range(100)이 0부터 99까지 숫자 100개를 생성 -> for 는 in으로
# 숫자를 하나씩 꺼내서 변수 i에 저장
# for i in range(100):
#      print('Hello, world!', i) -> range에서 순서대로 꺼낸숫자확인
# for i in range(5, 12) -> 5부터 11까지 반복
# range(10, 0, -1), range(0, 10, 2)
# 기존 range를 사용할때처럼 똑같이 여러 출력문을 만들 수 있음

# for i in reversed(range(10)): -> 숫자의 순서를 반대로 뒤집어서 출력

# 입력한 횟수대로 반복하기
# count = int(input('반복할 횟수를 입력하세요:')) -> int로 정수로 변환시켜줘야함
# for i in range(count):
#    print('Hello, world!', i)

# for letter in 'python':
#       print(letter, end = ' ')

# 구구단
# x = int(input())
# for i in range(1, 10):
#    print(x, '*', i, '=', x * i)

# i = 0
# while i < 100:
#    print('Hello, world!')
#    i += 1   # python은 증감연산자가 없기때문에 += 1로 증가시켜야함

import random  # random 모듈 가져옴
# print(random.random()) # random 모듈의 random함수 사용, 실수출력
# print(random.randint(1, 6)) # random 모듈의 randint, 정수 출력
''' while 문을 통한 random 수
    i = 0
    while i != 3:
        i = random.randint(1, 6)
        print(i)
'''
"""
    dice = [1, 2, 3, 4, 5, 6]
    random.choice(dice)
    -> .choice는 시퀀스 객체에서 요소를 무작위로 선택함
    -> tuple, range, list, 문자열 전부 가능
"""
# for 문은 반복횟수가 정해져있을때 사용
# while 문은 반복횟수가 정해져 있지 않을때 사용

# break 는 for와 반복문에서 제어 흐름을 벗어나기 위해 사용
# 즉 루프를 완전히 종료
# continue는 제어흐름(반복)은 유지한 상태에서 코드의 실행만 건너뜀

# i = 0
# while True:
#    if i % 10 != 3:
#        i += 1
#        continue # continue로 건너뛰게 되면 지금 루프의 밑에 있는
# i += 1도 건너뛰게 되므로 미리 i += 1을 통해 다음 루프로 진행될 수 있게함
#    elif i > 76:
#        break
#    print(i, end=' ')
#    i += 14
'''
    for i in range(5): # 5번 반복 바깥쪽 루프는 세로 방향
      for j in range(5): # 5번 반복 안쪽 루프는 가로 방향
         print('j:', j, sep = '', end = ' ') # j값 출력, sep 로 값사이 공백 없애고
        # end 로 마지막에 줄바꿈대신 한 칸 띠워줌
      print('i:', i, '\\n', sep = '') # \\n로 줄바꿈 되었다는 표시
    # print는 기본적으로 출력 후 다음 줄로 넘어감
'''
# for i in range(5):
#    for j in range(5):
#        print('*', end ='') # end에 ''를 지정하여 줄바꿈을 없앰
#    print() # 가로뱡향으로 별을 다 그린뒤 다음줄로 넘어감
# print는 기본적으로 end = '\n' 상태이므로 따로 줄바꿈지정 x
'''
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0: # i % 15 == 0으로도 가능
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)
'''

# for i in range(1, 101):
#    print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)
# Fizz *를 통해 3의 배수일때 Fizz를 출력
# + 연산자를 통해 3과 5의 배수이면 둘 다 true이므로 FizzBuzz출력
# 3과 5의 배수가 아닐경우 or 로 i값 그대로 출력
# 문자열을 곱하면 문자열이 반복되고 더하면 두 문자열이 연결됨
# 문자열에  * True(1)를 하면 문자열이 그대로나옴 False(0)를 곱하면 문자열 출력x

# x, y = map(int, input().split())

# for i in range(x, y + 1): # 두번째 정수까지 출력하기 위해 + 1
#    print('Fizz' * (i % 5 == 0) + 'Buzz' * (i % 7 == 0) or i)

# 리스트에 요소 추가
# append : 요소 하나를 추가, extend : 리스트를 연결하여 확장
# insert : 특정 인덱스에 요소 추가

# append는  리스트 끝에 하나의 요소를 넣을때 주로 사용
# a = [10, 20, 30] -> a.append(500)
# list안에 list 추가
# a = [10, 20, 30] -> a.append([500, 600])
# [10, 20, 30, [500, 600]]
# a.append는 [500, 600] 이라는 요소 하나를 a끝에 추가
# 때문에 len으로 길이를 구해보면 5가 아닌 4가 출력

# 리스트 끝에 추가할 요소가 많을 경우 extern
# a = [1, 2, 3] -> a.extend([5, 6]) -> [1, 2, 3, 5, 6] -> list와 list 연결

# insert 원하는 위치에 요소 추가
# a = [10, 20, 30] -> a.insert(2, 500) -> [10, 20, 500, 30]
# insert(0, 요소) : 리스트 맨처음에 요소 추가
# insert(len(리스트), 요소) : 리스트 끝에 요소 추가
# insert에 마지막 인덱스보다 큰 값을 지정하면 리스트 끝에 요소 하나 추가
# a = [10, 20, 30] -> a.insert(len(a), 500) -> [10, 20, 30, 500]

# 리스트 중간에 요소 여러개를 추가
# a = [10, 20, 30] -> a[1:1] = [500,600] -> [10, 500, 600, 20, 30]

# pop : 마지막 요소 또는 특정 인덱스의 요소를 삭제
# a = [10, 20, 30] -> a.pop() ->  [10, 20]
# a = [10, 20, 30] -> a.pop(1) -> [10, 30]
# del 을 사용해도 ㄱㅊ -> del a[1] -> [10, 30]

# remove : 특정값을 찾아서 삭제
# a = [10, 20, 30] -> a.remove(20) -> [10, 30]
# 같은 값이 여러개 있을 경우 처음 찾은 값만을 삭제

# 리스트에서 특정 값의 인덱스 구하기
# a = [10, 20, 30, 15, 20, 40] -> a.index(20) -> 1
# 같은 값이 여러개라면 가장 작은 인덱스 만을 찾음

# 특정값의 개수 구하기
# a = [10, 20, 30, 15, 20, 40] -> a.count(20) -> 2

# 리스트 순서 뒤집기 reverse()
# 리스트 요소 정렬 sort() -> 오름차순
# sort(reverse = True) -> 내림차순

# sort는 메서드를 사용한 리스트를 변경하지만 sorted는 새로운 리스트 생성
# a = [10, 20, 30, 15, 20, 40] 이 있으면 sort는 a의 리스트를 변경
# sorted는 새로운 리스트를 생성함

# 리스트 모든요소 삭제 -> a.clear() or del a[:]

# 리스트를 슬라이스로 조작
# a = [10, 20, 30] -> a[len(a):] = [500] -> [10, 20, 30, 500]

# 리스트가 비어 있는지 판단
# if not seq: -> 비어있다면 True
# if seq -> 내용이 있다면 True

# 리스트가 비어 있는지 확인 하는 방법은 마지막요소에 접근하는 방법이 유용하게 사용
# seq = [10, 20, 30] -> seq[-1] -> 30
# 만약 비어있다면 에러 발생
# 에러가 발생할때는 seq = [] if seq: print(seq[-1]) 로 확실히 확인

# 인덱스와 요소를 함께 출력
# a = [38, 21, 53, 62, 19]
# for index, value in enumerate(a): -> value를 안하면 (0, 38)로 소괄호가 출력됨
#    print(index, value)

# start로 원하는 인덱스 부터 출력
# a = [11, 22, 33, 44, 55]
# for index in enumerate(a, start = 1): -> enumerate(a, 1)로도 가능
#    print(index)

# 인덱스로 요소 출력하기
# a = [38, 21, 53, 62, 19]
# for i in range(len(a)):
#    print(a[i])

# while 문일 경우
# a = [38, 21, 53, 62, 19]
# i = 0
# while i < len(a):
#       print(a[i])
#       i += 1

# max, min 찾기

'''
1. c언어 에서 처럼
    a = [38, 21, 53, 62, 19]
    min = a[0]
    for i in a:
    if i < min:
    min = i
    print(min) -> 19

    max 는 부호를 반대로
    if i > max:
    max = i
    print(max) -> 62

2. sort를 이용
    가장 작은수     
    a [38, 21, 53, 62, 19] -> a.sort() -> a[0] -> 19
     가장 큰수
     a.sort(reverse = True) -> a[0] -> 62
   
3. max, min 함수를 사용
    a = [38, 21, 53, 62, 19] -> min(a) -> 19
    a = [38, 21, 53, 62, 19] -> max(a) -> 62

'''

# 요소의 합계 구하기 - 1번방법
# a = [10, 10, 10, 10, 10]
# x = 0
# for i in a:
#   x += i
# print(x) -> 50

# 요소의 합계 구하기 - 2번방법
# a = [10, 10, 10, 10, 10]
# sum(a)
# print(a) -> 50

# 리스트 생성
# a = [i for i in range(10)]
# b = list(i for i in range(10))
# c = [i + 5 for i in range(10)] // 0~9의 값에 5를 더하여 리스트생성
# d = [i * 2 for i in range(10)]

# a = [i for i in range(10) if i % 2 == 0]
# a -> [0, 2, 4, 6, 8] -> 짝수 리스트

# b = [i + 5 for i in range(10) if i % 2 == 1]
# [6,8,10,12,14]

# a = [i * j for j in range(2, 10) for i in range(1, 10)]
# -> 2단부터 9단까지의 구구단 리스트
# 리스트에 for 가 여러개일 때 처리 순서는 뒤에서 앞으로 진행한다

# a = [1.2, 2.5, 3.7, 4.6]
# for i in range(len(a)):
#     a[i] = int(a[i])
#   [1, 2, 3, 4]

# input().split() -> 는 문자열 리스트이다
# m = map(int, x) -> 리스트의 요소를 int로 변환, 결과는 맵 객체
# a, b = m -> 맵 객체는 변수 여러개에 저장할 수 있음

# a = (38, 21, 53, 62, 19, 53)
# a.index(53) -> 53의 가장 작은 인덱스(즉 처음 찾은 인덱스자리)출력
# a = (10, 20, 30, 15, 20, 40)
# a.count(20) -> tuple에서 특정값의 개수를 구함
'''
N, M = map(int, input().split())
    num[100] = {0,}
    max = 0;

    for i in range(N):
        num[i] = map(int, input())
        for j in range(N):
        sum = num[i] + num[j] + num[j + 1]
         if (sum > max and sum <= M):
            max = sum
    print(max)
'''
