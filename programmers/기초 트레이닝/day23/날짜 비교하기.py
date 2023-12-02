# 문제 설명
# 정수 배열 date1과 date2가 주어집니다. 두 배열은 각각 날짜를 나타내며 [year, month, day] 꼴로 주어집니다. 각 배열에서 year는 연도를, month는 월을, day는 날짜를 나타냅니다.
#
# 만약 date1이 date2보다 앞서는 날짜라면 1을, 아니면 0을 return 하는 solution 함수를 완성해 주세요.
#
# 제한사항
# date1의 길이 = date2의 길이 = 3
# 0 ≤ year ≤ 10,000
# 1 ≤ month ≤ 12
# day는 month에 따라 가능한 날짜로 주어집니다.
# 입출력 예
# date1	date2	result
# [2021, 12, 28]	[2021, 12, 29]	1
# [1024, 10, 24]	[1024, 10, 24]	0
# 입출력 예 설명
# 입출력 예 #1
#
# date1이 date2보다 하루 앞서기 때문에 1을 return 합니다.
# 입출력 예 #2
#
# date1과 date2는 날짜가 서로 같으므로 date1이 더 앞서는 날짜가 아닙니다. 따라서 0을 return 합니다.

# 처음에는 for문안에 조건문을 걸어서 풀었는데 테스트케이스 중 1개가 먹히지 않았다.
# 결국 원인을 찾지 못해서 아래와 같이 정확하게 푸는 방식을 사용했다.
# 다른 사람 풀이를 보니 if elif문을 사용해서 date1이 date2보다 작거나 큰 경우 return 0, 1을 걸어서
# 확실하게 표현해줬다.. 나는 if else 문으로만 조건을 걸어서 명확하지 않아 걸렸던것같디
def solution(date1, date2):
    str_date1 = ""
    str_date2 = ""
    for i in range(len(date1)):
        str_date1 += str(date1[i])
        str_date2 += str(date2[i])
    if int(str_date1) < int(str_date2):
        return 1
    else:
        return 0
    return 0


# 밑에 풀이는 레전드이다...
# int문이 list안에 있는 요소를 비교하고 부등호가 가능한 걸 처음알았다
# 파이썬 대단하다..
def solution(date1, date2):
    return int(date1 < date2)