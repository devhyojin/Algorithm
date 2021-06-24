def solution(bridge_length, weight, truck_weights):
    time = 0
    on_road = [0]*bridge_length
    while on_road:
        time += 1
        on_road.pop(0)
        if truck_weights:
            if sum(on_road) + truck_weights[0] <= weight:
                on_road.append(truck_weights.pop(0))
            else:
                on_road.append(0)
    return time

