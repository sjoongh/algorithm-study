def solution(numbers):
    numbers.sort(reverse=True)
    for i in range(max(numbers)):
        if numbers[i] < i-1:
            result = i
            break
    return result

print(solution([3, 0, 6, 1, 5])