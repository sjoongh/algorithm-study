"""
문자열 = string 

import math -> math 함수를 가져옴

.capitalize() -> 첫번째 문자만 대문자

.upper() -> 전부 대문자

.__len__() -> 문자열길이 출력

.replace -> 치환

divmod(5, 2)
(2, 1) -> 몫과 나머지 동시에 출력

print(10 / 4) -> 2.5 출력

a, b = input('문자열 두개 : ').split()
#스페이스바를 기준으로 변수에 입력값을 넣어줌
input() 만 쓰면 한번에 값 하나만 입력 받음
input().split()을 하면 여러개의 변수에 값을 입력할수있음
a = int(a)
b = int(b)
print(a + b)
# print(int(a) + int(b))

#spilit의 결과를 매번 int로 변환하지 않고 map과 같이 사용하면 된다
a, b = map(int, input('숫자 두개 : ').split(','))
# -> split의 분리할 기준 문자열을 콤마로 지정했으므로 10,20처럼 입력해야함
print(a + b)
# map() : 여러개의 데이터를 한번에 다른 형태로 변환, type이나 list, yuple 등등


# 값 사이에 공백이 아닌 다른 문자를 넣고 싶을 때
# sep는 구분자라는 뜻이다
'''
    print(1, 2, 3, sep= ', ')
    print(4, 5, 6, sep=',')
    print('hello','python', sep='')
    print(1920, 1080, sep='x')
    print(1, 2, 3, sep='\n')
'''

# end : 현재 print가 끝난뒤 그 다음에 오는 print 함수에 영향을 준다
# 원래 형식의 print 는 1\n2\n3으로 출력되지만 end=''을하면 123으로 출력
print(1, end='')
print(2, end='')
print(3)
# sep 는 현재 print문에 영향을 주고 sep는 다음 print문에 영향을 줌

"""

import math
print(math.ceil(2.24))
print(math.floor(2.24))
print(math.pow(2,10))
print(math.pi)

print('hello world'.capitalize())
print('hello wolrd'.upper())
print('hello wolrd'.__len__())
print('hello world'.replace('world','programming'))

name = "신중호"
print("안녕하세요"+name+"님")
print(name+"어서오세요")
#정수형과 print를 같이 쓸때는 str로 정수형 변수를 감싸줘야함 
# ex : age = 4 
# print("누구는"+str(age)+"살이에요")
# 정수형을 문자열로 바꿔줘야 같이 출력됨(정확한이유는??)
"""
변수가 print문자열 중간에 삽입되려면 +가 붙는다

if True:
    print("1")
    print("2")
print("3")

str = 22
real = 11
if real == str:
    print("hello")
else:

in_str = input("입력")
print(in_str+"world")

print(type(in_str))을 하면 변수 str이 어떤 type인지 확인가능

if real_egiong == in_str or real_k8805 == in str
c와 마찬가지고 if문에 여러 조건을 달 수 있으며
| 이나 or 둘 다 사용가능
& 이나 and 둘 다 사용가능
!= 이나 not 둘 다 사용 

while 문은 대부분의 프로그램언어에서 지원
for 문은 대부분은 아님
for문은 in 뒤의 값이 어떤 값들을 담고 있는 그릇일 경우에만 사용가능
while문은 true or false가 될수 있는 어떤값이든 사용가능

"""

print(type(['for', 'exam','ple']))
# class list로 표현된다

names = ['for','exam','25']
print(names)
#names에 담겨져있는 데이터 출력, type이 달라도 출력됨

print(names[1])
#배열

# min(num), max(num) -> num배열에서 가장 작은수와 가장 큰수

al = ['A','B','C','D']
print(len(al)) #al배열의 개수 출력
al.append('E') #al배열 마지막에 E추가
print(al)
del(al[0]) #al배열의 0번째값 삭제
print(al)

i = 0
while i < 10:
    print("hello world"+str(i*9))
    i = i + 1
#hello wolrd 9의 배수 10개 출력

members = ['shin','joong','ho']

for member in members: # for (반복문) in (list):
    print(member)
# in 뒤에 반복하고 싶은 배열 or 변수
# for 뒤에 변수를 선언해서 변수에 반복되는 값들을 담아냄

for item in [0,1,2,3,4]:
    print('hello')
#이런식으로도 변수자체를 넣어도됨

for item in range(5):
    print(item)
# 0, 1, 2, 3, 4 출력

for item in range(5, 11):
    print(item)
# 5, 6, 7, 8, 9, 10 출력

"""
def a3():
    print('aaa')
a3()
a3()를 하게 되면 a3()함수를 호출하므로 a3()함수의 print가 실행됨
"""

def a3():
    print('aaa')
a3()
a3()
a3()
# ('aaa')가 세번 출력

print('a'*3)
#aaa출력
def a3():
    return 'aaa'
# 함수에서 바로 출력하는 것 보다 함수밖에서 출력하는 것이 더
# 여러곳에서 함수를 활용할 수 있다.
print(a3())

def a(num): #a함수는 변수 num값을 불러옴
    return 'a'*num # 'a'는 *num의 개수만큼

print(a(2)) #aa가 출력

def make_string(str,num):
    return str*num
print(make_string('abc', 2))
# abc == str, 2 == num 이므로 -> abcabc 출력

"""
import egoing #eging 이라는 파일을 찾아서 실행
print(egoing.a())

from egoing import a -> a라는 함수를 불러옴 egoing으로부터
print(a()) -> 함수이름 print

from egoing import a as z -> as는 a라는 함수를 z로 변경해 사용
print(z())

import -> 모듈(math나 함수가 존재하는 파일같은 것, 함수를 담는 공간)
을 가져올수도 함수를 가져올수도 있음
"""
