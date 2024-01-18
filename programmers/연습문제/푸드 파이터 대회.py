def solution(food):
    eat_food = ''
    for idx, i in enumerate(food[1:]):
        # 각 음식을 반으로 나눔
        eat_food += str(idx+1) * (i//2)
        print(eat_food)
    result = eat_food + "0" + eat_food[::-1]
    return result