# 재귀를 돌리는 것보다 for문을 돌리는게 시간복잡도 효율이 좋다.

# for문을 사용할 경우
n = int(input())
# fibonacci의 입력값이 0이나 1일 경우를 생각해 0,1을 넣고
# 두가지 수를 계속 더해줘야 하므로 0,1을 넣음
fibonacci = [0, 1]
# n까지 반복
# 0과 1이 입력되면 어차피 for문은 안돌아가므로 그대로 출력
# 2는 for문이 한번 돌아가므로 1이 출력됨
for i in range(2, n+1):
    print('asb')
    # [i-1]과 [i-2]의 자리의 값을 더함
    num = fibonacci[i-1] + fibonacci[i-2]
    # fibonacci 리스트에 추가
    fibonacci.append(num)
# 정답 인덱스만을 출력
print(fibonacci[n])
