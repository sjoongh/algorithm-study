def check(w, h):
    # w와 h중 max=a, min=b
    a, b = max([w, h]), min([w, h])
    while True:
        # 최대 공약수 구함
        r = a % b
        # 최대공약수를 구한다면 return b
        if r == 0:
            return b
        # b에는 현재 r의 결과값이 들어가있으므로 max의 값은 필요없고 b의 min값을 비교해야함
        a = b
        # r의 현재 값을 b에 넣어줌
        b = r
        
def solution(w,h):
    # 사각형의 전체 크기
    square = w * h
    answer = check(w, h)
    
    # 전체크기 - ((w+h) - 최대공약수)
    return square - ((w+h) - answer)