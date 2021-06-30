def solution(bridge_length, weight, truck_weights):
    answer = 0

    bridge = []
    for _ in range(bridge_length):
        bridge.append(0)
    
    while truck_weights:
        bridge.pop(0)
        if truck_weights[0] + sum(bridge) <= weight:
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)
        answer += 1

    while bridge:
        answer += 1
        bridge.pop()

    return answer

print(solution(2, 10, [7, 4, 5, 6]))