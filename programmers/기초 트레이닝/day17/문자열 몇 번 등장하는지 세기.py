# 문자열 myString과 pat이 주어집니다. myString에서 pat이 등장하는 횟수를 return 하는 solution 함수를 완성해 주세요.

# 제한사항
# 1 ≤ myString ≤ 1000
# 1 ≤ pat ≤ 10
# 입출력 예
# myString	pat	result
# "banana"	"ana"	2
# "aaaa"	"aa"	3
# 입출력 예 설명
# 입출력 예 #1

# "banana"에서 1 ~ 3번 인덱스에서 한 번, 3 ~ 5번 인덱스에서 또 한 번 "ana"가 등장해서 총 두 번 등장합니다. 따라서 2를 return 합니다.
# 입출력 예 #2

# "aaaa"에서 0 ~ 2번 인덱스에서 한 번, 1 ~ 3번 인덱스에서 한 번, 2 ~ 4번 인덱스에서 한 번 "aa"가 등장해서 총 세 번 등장합니다. 따라서 3을 return 합니다.

def solution(myString, pat):
    start = 0
    cnt = 0

    while True:
        # start를 인덱스로 활용하며 myString에서 pat에 해당하는 문자를 찾는다
        # 해당하는 문자열을 찾을 경우 idx에 그대로 넣어주고 그 다음 순서로 넘어가기 위해 += 1
        # 문자를 찾았으므로 cnt도 늘려주고 find로 더 이상 찾을게 없으면 idx = -1 이므로 while문을 탈출하며 종료
        idx = myString.find(pat, start)
        if idx == -1:
            break
        cnt += 1
        start = idx + 1

    return cnt