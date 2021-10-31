def solution(numbers):
    # numbers의 요소 str로 변환
    numbers = list(map(str, numbers))
    # numbers의 요소는 1000이하이므로 3자리 수로 맞춘 뒤 비교
    # str 비교는 아스키코드 값으로 비교됨, 큰 수 부터 reverse로 정렬
    numbers.sort(key=lambda x:x*3, reverse=True)
    # join으로 ,제거
    return str(int(''.join(numbers)))