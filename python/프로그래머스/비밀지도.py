def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        # bit연산으로 or연산자 사용해 넣어줌
        tmp = bin(arr1[i] | arr2[i])
        # 파이썬 이진법은 앞에 문자 두글자가 붙기 때문에 2:부터 넣어줌
        # 숫자를 출력할때 앞에 0을 붙여주고 싶다면 zfill()사용
        # tmp = tmp[2:].zfill(n)
        tmp = tmp[2:]
        # tmp의 크기가 n(지도크기)보다 작다면 앞에 0을 붙여줌
        if len(tmp) < n:
            tmp = '0' * (n-len(tmp)) + tmp
        # replace를 두개사용해 1은 #으로 0은 ' '으로 변경 
        tmp = tmp.replace('1', '#').replace('0', ' ')
        answer.append(tmp)
    return answer
