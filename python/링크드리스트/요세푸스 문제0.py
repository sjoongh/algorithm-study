# 처음 생각 : 재귀or 반복문으로 배열의 값이 0이 될때까지 반복함
# 반복문처리과정에서 문제 발생ㅠ

# Soluton1 !!
n, k = map(int, input().split())
arr = [i for i in range(1, n + 1)]
answer = []
# pop는 무조건 배열의 인덱스를 기준으로 값을 꺼내오므로
# arr배열의 시작이 1이여도 pop속성이 보기에는 인덱스 0을 가르킴
# 그러므로 k-1을 통해 알맞은 인덱스로 찾아갈 수 있게 설정
num = k - 1

for i in range(n):
    if len(arr) > num:
        answer.append(arr.pop(num))
        num += k - 1
    elif len(arr) <= num:
        # num값이 인덱스의 값을 넘어가면 len(arr)의 배열만큼 나눠줌
        num = num % len(arr)
        answer.append(arr.pop(num))
        num += k -1
# answer는 배열 상태이므로 요소를 하나씩 반복문으로 꺼내야함
# join은 문자를 문자열로 합쳐주는 기능이므로 str(i)로 변경후 ",".join으로 구분해줌
# 또한 각 요소의 공백은 없으므로 sep=""로 설정
print("<", ', '.join(str(i) for i in answer), ">", sep = '')


# Solution 2!!!!
# N, K = map(int, input().split())

# arr = [i for i in range(1, N+1)]
# result = []
# num = 0
# for i in range(N):
#     num += K-1
#     if num >= len(arr):
#         num값이 len(arr)과 같거나 커지는 순간부터 len(arr)의 배열을 넘어가면 안되므로 %로 나머지값을 넣어주고 위의 num += K-1조건과 연계하여
#         자동으로 조건에 맞추어 원을 계속 돌아감 --> num에는 계속 K-1의 값이 들어가므로 원이 돌아갈 수 있게 함
#         num = num % len(arr)
#     result.append(arr.pop(num))
# print("<", ", ".join(str(i) for i in result), ">", sep="")
    