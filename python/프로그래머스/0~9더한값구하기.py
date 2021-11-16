# 방법 1. 프로그래머스 문제 numbers의 배열이 number에 존재하면 빼야함, numbers에 없는 0~9의 숫자만 더해서 출력
# number안에 numbers가 존재하면 전부 remove -> for in
# 나머지값 반복문으로 출력
# numbers = [1,2,3,4,5,6,7,8,0]
def solution(numbers):
    result = 0
    number = [0,1,2,3,4,5,6,7,8,9]
    for i in numbers:
        if i in number:
            number.remove(i)
    for j in range(len(number)):
        result += number[j]
    return result
# print(solution(numbers))

# 방법 2.
# remove한 값을 전부 더해줌
# 0~9를 더한 45에서 빼줌
# def solution(numbers):
#     answer = 45
#     result = 0
#     number = [0,1,2,3,4,5,6,7,8,9]
#     for i in numbers:
#         for j in number:
#             if i == j:
#                 number.remove(j)
#                 break
#         result += j
#     return answer - result