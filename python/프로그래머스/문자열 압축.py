def solution(s):
    # 최소길이
    answer = len(s)

    # 자르는 단위 늘려가며 최소 길이 계산
    for i in range(1, len(s) //2+1):
        result = "" # 압축된 문자열
        count = 1 # 반복 횟수
        compare = s[0:i] # 자른 문자열

        # 압축된 문자열 구하기
        for j in range(i, len(s), i):
            # 문자열이 반복 되는 경우
            if compare == s[j:j+i]:
                count += 1
            # 더 이상 압축할 수 없을 경우
            else:
                if count == 1:
                    result += compare
                    compare = s[j:j+i]
                else:
                    result += (str(count) + compare)
                    count = 1
                    compare = s[j:j+i]
        # 나머지 문자열 처리
        if count == 1:
            result += compare
        else:
            result += (str(count) + compare)

        # 최소 길이 계산
        answer = min(answer, len(result))

    return answer