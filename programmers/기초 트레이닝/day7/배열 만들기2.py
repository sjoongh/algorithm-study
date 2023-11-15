# 문제 설명
# 정수 l과 r이 주어졌을 때, l 이상 r이하의 정수 중에서 숫자 "0"과 "5"로만 이루어진 모든 정수를 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.

# 만약 그러한 정수가 없다면, -1이 담긴 배열을 return 합니다.

# 제한사항
# 1 ≤ l ≤ r ≤ 1,000,000
# 입출력 예
# l	r	result
# 5	555	[5, 50, 55, 500, 505, 550, 555]
# 10	20	[-1]
# 입출력 예 설명
# 입출력 예 #1

# 5 이상 555 이하의 0과 5로만 이루어진 정수는 작은 수부터 5, 50, 55, 500, 505, 550, 555가 있습니다. 따라서 [5, 50, 55, 500, 505, 550, 555]를 return 합니다.
# 입출력 예 #2

# 10 이상 20 이하이면서 0과 5로만 이루어진 정수는 없습니다. 따라서 [-1]을 return 합니다.

# 풀이 1.
def solution(l, r):
    answer = []
    for i in range(l, r + 1):
        if str(i).count('0') + str(i).count('5') == len(str(i)):
            answer.append(i)
    return answer

print(solution(5, 555))

# 풀이 2.
def solution(l, r):
    answer = []
    for i in range(l, r + 1):
        # 아래 로직 설명 : 53이 들어왔을 때 53을 str로 바꾸면 '53'이 되고 이걸 for문으로 돌리면 '5'와 '3'이 나옴 -> 이걸 all로 돌리면 5와 3이 all에 들어가서 False가 나옴 -> 그래서 53은 answer에 들어가지 않음
        # 결과적으로 5와 0만 들어간 숫자만 True가 나옴
        if all(j in ['0', '5'] for j in str(i)):
            answer.append(i)
    return answer

print(solution(5, 555))

def solution(l, r):
    answer = []
    for i in range(l, r+1):
        if str(i).count('0') == len(str(i)) or str(i).count('5') == len(str(i)) or str(i).count('0') + str(i).count('5') == len(str(i)):
            answer.append(i)
    if len(answer) == 0:
        return [-1]

    return answer