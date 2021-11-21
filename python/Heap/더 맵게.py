import heapq

def solution(scoville, K):
    heap = []
    answer = 0
    for num in scoville:
        # heapq.heappush(대상리스트, 넣을 요소)
        heapq.heappush(heap, num)
    while heap[0] < K:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        except IndexError:
            return -1
        answer += 1
    return answer

# Heap을 사용하지 않으면 효율성에서 문제 발생
# def solution(scoville, K):
#     answer = 0
#     while min(scoville) < K:
#         scoville.sort()
#         # 에러 처리
#         try:
#             if scoville[0] < K:
#                 scoville.insert(0, scoville.pop(0)+(scoville.pop(0) * 2))
#         # 모든 음식을 k이상으로 만들 수 없는 경우 -1을 return
#         # 범위를 벗어난 index발생 시 error
#         except IndexError:
#             return -1
#         answer += 1
#     return answer