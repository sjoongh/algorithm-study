# 폰켓몬, [3,1,2,3], 중복제거 & nums // 2만큼 출력
def solution(nums):
    return min(len(nums) // 2, len(set(nums)))

# 폰켓몬, 내 방법
def solution(nums):
    answer_nums = 0
    answer_nums1 = 0

    answer_nums = set(nums)
    answer_nums1 = len(nums) // 2
    if len(answer_nums) > answer_nums1:
        return answer_nums1
    else:
        return len(answer_nums)


print(solution([3,  1, 2, 3]))
