# 순열을 떠올리고
# result[n-3] = result[n-1] + result[n-2]로 표현이 가능하다는것을 기억하자
n = int(input())
result = [0, 1, 2]
for i in range(3, 1001):
    result.append(result[i-1] + result[i-2])
print(result[n] % 10007)