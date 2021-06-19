def solution(priorities, location):
    answer = 0

    idx = []
    for _ in range(len(priorities)):
        idx.append(False)
    idx[location] = True
    cnt = 0

    while True:
        if priorities[0] == max(priorities):
            if idx[0]:
                print(cnt)
                break
            else:
                cnt += 1
                priorities.pop(0)
                idx.pop(0)
        else:
            priorities.append(priorities.pop(0))
            idx.append(idx.pop(0))

    answer = cnt + 1

    return answer

print(solution([1, 1, 9, 1, 1, 1], 0))