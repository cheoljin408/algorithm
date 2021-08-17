from itertools import combinations
def solution(numbers):
    answer = []
    set_answer = set()
    
    for i in list(combinations(numbers, 2)):
        answer.append(sum(i))
    
    set_answer = set(answer)
    answer = list(set_answer)
    answer.sort()
    
    return answer

print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))