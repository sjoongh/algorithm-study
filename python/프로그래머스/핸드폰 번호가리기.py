def solution(phone_number):
    answer = ''
    number = len(phone_number) - 4
    answer = ('*'* number) + phone_number[number:]
    return answer