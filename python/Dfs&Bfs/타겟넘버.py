# bfs 방식
from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0],0])
    queue.append([-1*numbers[0],0])
    while queue:
        tmp, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append([tmp+numbers[idx], idx])
            queue.append([tmp-numbers[idx], idx])
        else:
            if tmp == target:
                answer += 1
    return answer

# dfs방식
def solution(numbers, target):
    # tree는 이전수에 대한 계산 결과를 담은 층
    tree = [0]
    # 숫자 목록을 하나씩 꺼내와 주는 역할
    for num in numbers:
        sub_tree = []
        # 노드 하나하나에 숫자를 더하고 빼주어 자식 노드를 생성
        for tree_num in tree:
            sub_tree.append(tree_num + num)
            sub_tree.append(tree_num - num)
        # sub_tree는 현재 숫자에 대한 결과를 담은 자식 노드를 하나씩 추가
        tree = sub_tree
    return tree.count(target)