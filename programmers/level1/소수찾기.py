def solution(n):
    answer = 0
    list_flag = [False, False] + [True] * (n-1)

    for i in range(2, n+1):
        if list_flag[i]:
            for j in range(2*i, n+1, i):
                list_flag[j] = False
    for i in range(len(list_flag)):
        if list_flag[i]:
            answer += 1
    
    return answer

print(solution(10))
print(solution(5))