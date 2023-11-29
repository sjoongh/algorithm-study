def solution(arr):
    answer = []
    two = 0
    if len(arr) == 0:
        return arr
    for i in range(len(arr)):
        if len(arr) > two:
            if two == 0:
                two += 2
            else:
                two *= 2
        else:
            arr += [0] * (two-len(arr))
            break
    return arr