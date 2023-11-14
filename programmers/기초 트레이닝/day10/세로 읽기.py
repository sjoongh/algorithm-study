# 문자열 my_string과 두 정수 m, c가 주어집니다. my_string을 한 줄에 m 글자씩 가로로 적었을 때 왼쪽부터 세로로 c번째 열에 적힌 글자들을 문자열로 return 하는 solution 함수를 작성해 주세요.
#
# 제한사항
# my_string은 영소문자로 이루어져 있습니다.
# 1 ≤ m ≤ my_string의 길이 ≤ 1,000
# m은 my_string 길이의 약수로만 주어집니다.
# 1 ≤ c ≤ m
# 입출력 예
# my_string	m	c	result
# "ihrhbakrfpndopljhygc"	4	2	"happy"
# "programmers"	1	1	"programmers"
# 입출력 예 설명
# 입출력 예 #1
#
# 예제 1번의 my_string을 한 줄에 4 글자씩 쓰면 다음의 표와 같습니다.
#
# 1열	2열	3열	4열
# i	h	r	h
# b	a	k	r
# f	p	n	d
# o	p	l	j
# h	y	g	c
# 2열에 적힌 글자를 세로로 읽으면 happy이므로 "happy"를 return 합니다.
#
# 입출력 예 #2
#
# 예제 2번의 my_string은 m이 1이므로 세로로 "programmers"를 적는 것과 같고 따라서 1열에 적힌 글자를 세로로 읽으면 programmers입니다. 따라서 "programmers"를 return 합니다.

# 내 풀이
def solution(my_string, m, c):
    answer = ''
    count = c -1
    print(list(my_string))
    for i in range(len(my_string)):
        if (c-1) == i:
            answer += my_string[i]
            count += m
        if count == i:
            answer += my_string[i]
            count += m
    return answer

# 다른 사람 풀이..
# 문자열을 짤라서 만들 수 있다는걸 알고 있었는데 생각이 나질 않았다.. 역시 응용을 잘해야..
def solution(s, m, c):
    # 문자열 s에서 c-1로 0번째부터 시작하기 위해 맞춰주고 m의 크기로 올라가며 끝까지 탐색한다
    # 파이썬 슬라이싱은 [start:end:idx] 순서이므로 [start::idx] 만 사용한 문법이라고 볼 수 있다.
    # [s:e+1][::-1] 이런식으로 뒤에서부터 순차적으로 내려올때 앞에 [s:e+1]로 조건부 영역을 지정할 수 있는 것 같다.
    return s[c-1::m]

print(solution("ihrhbakrfpndopljhygc", 4, 2))