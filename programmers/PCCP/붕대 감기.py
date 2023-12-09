# 붕대 감기 -> t초 동안 1초마다 x만큼의 체력 회복
# t초 연속 붕대를 감는데 성공한다면 y만큼의 체력을 추가로 회복
# 현재체력이 최대 체력보다 커지는것은 불가능
# 공격을 당하면 기술취소 & 회복 못함
# 몬스터에게 공격당해 기술이 취소당하거나 기술이 끝나면 즉시 붕대감기 사용 && 연속 성공시간 0으로 초기화
# 시전시간, 1초당 회복량, 추가 회복량 = bandage 배열
# 최대체력 = health
# 몬스터의 공격시간과 피해량 = attacks
# 공격을 받고 캐릭터의 체력이 0이하로 내려가 사망하면 -1
# 아니라면 남은체력 return

def solution(bandage, health, attacks):
    answer = 0
    success = 0
    origin_health = health
    len_attacks = attacks[-1][0]+1
    for i in range(len_attacks):
        if attacks[0][0] == i:
            health -= attacks[0][1]
            attacks.pop(0)
            success = 0
        # else:
        #     success += 1
        #     if success == bandage[0]:
        #         health += bandage[2] + bandage[1]
        #         success = 0
        #         continue
        #     # 해당 부분이 잘못되어서 자꾸 실패했던 거였음 예를 들어 30 > 29라면 조건에 부합해서
        #     # 최대체력을 넘어서는 값을 받게 되는데 최대체력을 넘기면 안되므로 오류가 있었음..
        #     # 코드 실행에서는 교묘하게 이런 케이스를 없애놔서 테스트케이스에서 전부 실패ㅠ
        #     if origin_health > health+bandage[1]:
        #         health += bandage[1]
        # 정답으로 맞춘 코드는 아래와같다.
        else:
            health += bandage[1]
            success += 1
            if success == bandage[0]:
                health += bandage[2]
                success = 0
            if origin_health < health:
                health = origin_health
        if health <= 0:
            return -1
    return health

# 붕대 감기 -> t초 동안 1초마다 x만큼의 체력 회복
# t초 연속 붕대를 감는데 성공한다면 y만큼의 체력을 추가로 회복
# 현재체력이 최대 체력보다 커지는것은 불가능
# 공격을 당하면 기술취소 & 회복 못함
# 몬스터에게 공격당해 기술이 취소당하거나 기술이 끝나면 즉시 붕대감기 사용 && 연속 성공시간 0으로 초기화
# 시전시간, 1초당 회복량, 추가 회복량 = bandage 배열
# 최대체력 = health
# 몬스터의 공격시간과 피해량 = attacks
# 공격을 받고 캐릭터의 체력이 0이하로 내려가 사망하면 -1
# 아니라면 남은체력 return

def solution(bandage, health, attacks):
    answer = 0
    success = 0
    origin_health = health
    len_attacks = attacks[-1][0]+1
    for i in range(len_attacks):
        if attacks[0][0] == i:
            health -= attacks[0][1]
            attacks.pop(0)
            success = 0
        else:
            health += bandage[1]
            success += 1
            if success == bandage[0]:
                health += bandage[2]
                success = 0
            if origin_health < health:
                health = origin_health
        if health <= 0:
            return -1
    return health