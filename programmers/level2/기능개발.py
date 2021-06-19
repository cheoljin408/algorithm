def solution(progresses, speeds):
    answer = []

    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        cnt = 0
        while progresses:
            if progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                cnt += 1
            else:
                break
        if cnt > 0:
            answer.append(cnt)

    return answer

print(solution([93, 30, 55], [1, 30, 5]))