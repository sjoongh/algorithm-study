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
                # 문자열 반복 count
                count += 1
            # 더 이상 압축할 수 없을 경우
            else:
                # count가 1일 경우 result에 자른문자열(compare)값을 더해주고
                # 다음 문자열로 넘어가 반복되는지 확인하기 위해 compare는 다음 문자열로 초기화
                if count == 1:
                    result += compare
                    compare = s[j:j+i]
                # count가 1이 아닐 경우
                # 반복횐 횟수(str(count))와 compare를 result에 저장하고
                # compare와 count 모두 초기화
                else:
                    result += (str(count) + compare)
                    count = 1
                    compare = s[j:j+i]
        # for문이 다 끝나도 처리되지 않은 나머지 문자열 처리
        if count == 1:
            result += compare
        else:
            result += (str(count) + compare)

        # 최소 길이 계산
        answer = min(answer, len(result))

    return answer