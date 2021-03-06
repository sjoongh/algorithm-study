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

# 해결
def solution(number, k):
    answer = []
    for num in number:
        # answer에 뭐라도 존재하고, k가 0보다 크며, answer의 맨 뒤 값이 현재의 num보다 작으면
        while answer and k > 0 and answer[-1] < num:
            # answer의 맨 위 값을 제거하고 k도 -1 해준다
            answer.pop()
            k -= 1
        # 현재의 num값은 무조건적으로 answer에 넣어준다
        answer.append(num)
    
    # answer는 number의 길이 - k만큼 슬라이싱 해준다.
    # -> 슬라이싱은 index 바깥으로 나가도 괜찮음! 
    # 일반적으로 k는 0일텐데 ex) k = 3 number = 1000000 이런 경우엔 k는 처음 인풋받은 그대로 유지됨
    # 이럴 때 답은 뒷 숫자를 k개만큼 없애준 1000 이므로 슬라이싱을 len(number) - k로 해주는 것
    answer = ''.join(answer[:len(number)-k]) # 시작점부터 특정 위치까지 -> len(number) - k를 통해 1000000 --> 1000만 가져옴
    # [len(number) -k:] -> 시작점부터 끝까지
    
    return answer