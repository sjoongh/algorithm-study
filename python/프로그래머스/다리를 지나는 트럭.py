def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    
    while len(bridge):
        answer += 1
        bridge.pop(0)
        
        if truck_weights:
      # 다리를 지나가는 트럭 = bridge
      # track_weights 새롭게 들어올트럭
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return answer
