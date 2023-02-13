n = int(input())

array=list(map(int, input().split()))

# n만큼 배열 생성
d = [1 for i in range(n)]
for i in range(1,n):
    for j in range(i):
        # 자기 자신의 인덱스보다 작은 인덱스의 숫자들 중 자기 자신의 값보다
        # 큰 값의 인덱스를 구하고 d에 인덱스에 해당하는 dp값을 넣어준다
        if array[j]>array[i]:
            d[i] = max(d[i], d[j]+1)
print(max(d))