# 3kg포대와 5kg포대로 가장 적은 포대가 나오는 방법
n = int(input())

answer = 0
while n >= 0:
    # 5kg포대로만 이루어진 것이 가장 작으므로 나눠진다면 바로 출력
    if n % 5 == 0:
        answer += n // 5
        print(answer)
        break
    # 아닐경우 3kg포대를 빼줌
    n -= 3
    # answer 또한 포대개수를 늘려줌
    answer += 1
# while문의 break에 안걸릴경우 n개마늠의 포대를 만들 수 없으므로 -1
else:
    print(-1)
