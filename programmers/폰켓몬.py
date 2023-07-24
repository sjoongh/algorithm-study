def solution(nums):
    answer = 0
    size = len(nums) // 2
    if size > len(set(nums)):
        answer = len(set(nums))
    else:
        answer = size
    return answer