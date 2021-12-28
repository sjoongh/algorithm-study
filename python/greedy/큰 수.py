# 1. 실패 -> answer_li의 값이 고정이라
# def solution(number, k):
#     answer = 0
#     num_li = list(number)
#     # len(number)값에서 k를 뺀 값을 기준으로 반복문 돌림
#     num_len = len(num_li) - k
#     # i는 처음부터 돌아감 현재 위치의 i가 len값이 k-1이 될때까지 값을 append
#     for i in range(len(num_li)):
#         answer_li = ''
#         if len(str(i)) < k:
#             answer_li=''.join(num_li[:num_len-1]) # num_li가 빼낸값은 number에서 pop해야함
#             print(answer_li)
#         for j in range(1+i, len(num_li)):
#             # print(int(str(answer_li)+str(num_li[j])))
#             if int(str(answer_li)+str(num_li[j])) > answer:
#                 answer = int(str(answer_li) + str(num_li[j]))
#         num_li.pop(0)
#     return str(answer)
