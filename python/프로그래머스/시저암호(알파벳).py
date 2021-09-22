# 1. 알파벳 대소문자 구분
# 2. s[i]의 위치를 찾기 위해 -ord('A')+n을 해줌
# 3. 26으로 나눠주는 이유는 각자의 현재 위치에서 각자의 소문자, 대문자 영역을 벗어나지 않고
# 4. 범위안에서 n값만큼만 돌아갈 수 있게 설정하는 것
def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]= chr((ord(s[i])-ord('A')+n)%26+ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i])-ord('a')+n)%26+ord('a'))
    return "".join(s)
print(solution("a A b B g G z Z", 1))