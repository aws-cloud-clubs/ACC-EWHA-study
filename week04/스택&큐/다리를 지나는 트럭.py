def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length
    
    while truck_weights:
        time += 1
        bridge.pop(0)
        
        if sum(bridge) + truck_weights[0] <= weight:
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)
    
    # 모든 대기 트럭이 빠져나가면
    time += bridge_length

    return time