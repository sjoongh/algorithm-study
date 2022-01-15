import sys

N = int(sys.stdin.readline())
answer = [0] * (N + 2)	# answer에 계산된 값을 저장해둔다.
# --> 0과 1이 입력될우 [0, 0]이 출력되어야 하므로 +2을 통해 자리를 만듬

# range는(시작, 끝-1)까지 돌아가므로 10까지 돌아가게 하기 위해 +1을 해야함
for i in range(2, N+1): # 0과 1은 count가 0이므로 제외하고 시작하기 위해 2부터 시작함
    # if문만을 이용해야 세 연산을 다 거칠 수 있다.
    # answer[i] = count숫자(즉 계산내역, -1 or % 2 or % 3)가 들어감
    answer[i] = answer[i - 1] + 1 # 밑에 두가지의 if문에 걸리지 않는다면 (ex : 5, 7, 11) 
    # --> answer[i-1] = 그전에 계산했던 count수 이므로 answer[i-1] + 1을 통해 -1이 계산되었다는것을 count해준뒤 다시 계산 
    # 2나 3으로 나누어질때 answer[i-1]과 비교하여 최소값을 answer[i]에 넣어줌
    if i % 3 == 0:
        answer[i] = min(answer[i], answer[i // 3] + 1)	# 1을 더하는 것은 answer는 결과가 아닌 계산한 횟수를 저장하는 것 이기 때문이다.
        # answer[i]에 더하지 않는 이유는 이미 1을 뺄 때 1을 더해준 이력이 있기 때문이다.
    if i % 2 == 0:
        answer[i] = min(answer[i], answer[i // 2] + 1)
print(answer[N])