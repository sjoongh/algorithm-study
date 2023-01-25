n = int(input())

result = [0, 1, 3]

for i in range(3, 1001):
    result.append(result[i-1]+result[i-2]+result[i-2])
print(result[n] % 10007)