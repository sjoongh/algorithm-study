def solution(binomial):
    # eval : 매개변수로 받은 expression(=식)을 문자열로 받아서 실행하는 함수이다.
    # expression은 파이썬에서 실행 가능한 문자열이 들어와야 한다는 것이다.
    return eval(binomial)

print(solution("43 + 12"))