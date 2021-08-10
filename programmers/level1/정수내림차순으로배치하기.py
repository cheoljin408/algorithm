def solution(n):
    answer = 0
    num_list = list(map(int, str(n)))
    num_list.sort()
    
    for i in range(len(num_list)):
        answer += num_list[i]*(10**i)
    
    return answer

print(solution(118372))