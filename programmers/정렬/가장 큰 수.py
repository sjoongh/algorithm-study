def solution(numbers):
    numbers = list(map(str, numbers))
    # lambda를 활용하여 주어진 숫자가 1000 미만이므로 3자리수까지 모든 경우의수를 늘려서 비교함 -> 어차피 늘리면 앞에 자리가 큰게 이김
    # 비교한 숫자를 내림차순으로 정렬함
    numbers.sort(key=lambda x:x*3, reverse=True)
    # int를 붙여주는 이유는 특이케이스 [0,0,0,0] 이 존재하기 때문
    # 0000이 아닌 0이 결과값이여야 하므로 int로 변경후 str로 출력
    return str(int(''.join(numbers)))