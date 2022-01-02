import sys

N = int(sys.stdin.readline())
answer = [0] * (N + 1)	# answer에 계산된 값을 저장해둔다.
# --> range가 2부터 시작이므로 +1을 해줌 10이 들어오면 11만큼 배열 생성

# range는(시작, 끝-1)까지 돌아가므로 10까지 돌아가게 하기 위해 +1을 해야함
for i in range(2, N + 1): # 0과 1은 count가 0이므로 제외하고 시작하기 위해 2부터 시작함
# 여기서 2 나누기, 3 나누기 동등하게 하지 않고 처음에 1을 빼고 시작하는지 의아해 할 수 있다.
# 1을 빼고 시작하는 이유는 다음에 계산할 나누기가 1을 뺀 값보다 작거나 큼에 따라 어차피 교체되기 때문이다.
# 즉 셋 다 각각 시도하는 방법이 맞다.
# 여기서 if elif else를 사용하면 안된다. if만 이용해야 세 연산을 다 거칠 수 있다.
    answer[i] = answer[i - 1] + 1
    # 2나 3으로 나누어질때 answer[i-1]과 비교하여 최소값을 answer[i]에 넣어줌
    if i % 3 == 0:
        answer[i] = min(answer[i], answer[i // 3] + 1)	# 1을 더하는 것은 answer는 결과가 아닌 계산한 횟수를 저장하는 것 이기 때문이다. 
        # answer[i]에는 더하지 않는 이유는 이미 1을 뺄 때 1을 더해준 이력이 있기 때문이다.
    if i % 2 == 0:
        answer[i] = min(answer[i], answer[i // 2] + 1)
print(answer[N])