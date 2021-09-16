def solution(s):
    # 공백을 기준으로 나눔
    s_split = s.split(' ')
    # 공백을 기준으로 나눈 각각의 요소 출력
    for i in range(len(s_split)):
        # 리스트 형식으로 만듬
        s_list = list(s_split[i])
        for j in range(len(s_list)):
            if j % 2 == 0:
                s_list[j] = s_list[j].upper()
            elif j % 2 == 1:
                s_list[j] = s_list[j].lower()
        s_split[i] = "".join(s_list)
    # list를 str로 
    answer = " ".join(s_split)
    return answer

#     def toWeirdCase(s):
#     a=[]
#     s=s.split(" ")
#     for i in range(len(s)):
#         for j in range(len(s[i])):
#             if j%2==0:
#                 a.append(s[i][j].upper())
#             else:
#                 a.append(s[i][j].lower())
#         a.append(" ")

#     c="".join(a[:-1])
#     return c

# print("결과 : {}".format(toWeirdCase("try hello world")));