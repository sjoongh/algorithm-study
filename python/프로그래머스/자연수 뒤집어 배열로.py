def solution(n):
    # 정수를 list(str)로 변환
    n = list(str(n))
    # str list는 reverse(뒤집기)가 가능함
    n.reverse()
    # 정수형으로 ''을 없애줘야 하므로 요소들을 map(int)로 바꿔준뒤 list형식으로 출력
    return list(map(int, n))