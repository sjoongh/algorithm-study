result = 0
arrList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ["SUN", "MON","TUE", "WED", "THU", "FRI", "SAT"]
x, y = map(int, input().split())

for i in range(x-1):
    result += arrList[i]
result = (result + y) % 7
print(day[result])
