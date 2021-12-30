# # 3           -> 3번 테스트 할 것
# # n은 인쇄되는 페이지 개수
# # m은 몇번째 페이지가 궁금한지 나타냄
# # 1 0         -> n = 1, m = 0
# # 5           -> 인쇄되는 페이지 중요도 = 5,
# # 4 2         -> n = 4, m = 2
# # 1 2 3 4     -> 중요도 = 1 2 3 4
# # 6 0         -> n = 6, m = 0
# # 1 1 9 1 1 1 -> 중요도 = 1 1 9 1 1 1

import sys

num = int(input())

for _ in range(num):
    n,m = list(map(int, input().split()))
    n_li = list(map(int, input().split()))
    find = list(range(len(n_li))) # n_li의 길이만큼 리스트만듬
    find[m] = 'target'
    
    order = 0
    # 입력 후에 결과를 도출해야 하므로 while문이 for문 안에 존재
    while True:
        if n_li[0] == max(n_li):
            order += 1
        
            if find[0] == 'target':
                print(order)
                break
            else:
                n_li.pop(0)
                find.pop(0)
        else:
            n_li.append(n_li.pop(0))
            find.append(find.pop(0))