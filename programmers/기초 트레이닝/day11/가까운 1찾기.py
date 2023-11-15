def solution(arr, idx):
    count = 0
    for i in arr[idx:]:
        if i == 1:
            return idx+count
        count += 1
    return -1