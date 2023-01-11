n = int(input())
result = map(int, input().split())
max = 1000000
min = -1000000

for i in result:
    if (i < min):
        min = i
    if (i > max):
        max = i
print(min,max)