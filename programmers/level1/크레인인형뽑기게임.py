def solution(board, moves):
    answer = 0
    push = []

    for i in moves:
        for j in board:
            if j[i - 1] != 0:
                push.append(j[i - 1])
                if (len(push) > 1) and (push[len(push) - 1] == push[len(push) - 2]):
                    push.pop()
                    push.pop()
                    answer = answer + 2
                j[i - 1] = 0
                break

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))