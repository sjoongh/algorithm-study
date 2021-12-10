def solution(bridge_length, weight, truck_weights):
    answer = 0
    # bridge는 다리의 길이를 표현하는 동시에 트럭이 지나가는 다리역할과 while문이 돌아가는 루프로 만듬
    # --> return 값은 다리를 지나갈때 트럭이 다리의 길이만큼 + 지나가는 시간을 계산해야 하므로
    bridge = [0] * bridge_length
    
    while len(bridge):
        answer += 1
        bridge.pop(0)
        # track_weights에 값이 존재한다면 조건에 부합
        if truck_weights:
      # 다리를 지나가는 트럭 = bridge
      # track_weights 새롭게 들어올트럭
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return answer
