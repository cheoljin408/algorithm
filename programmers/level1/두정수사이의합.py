def solution(a, b):
    answer = 0
    if a == b:
        return a
    if max(a, b) == b:
        a, b = b, a
    
    answer = sum(range(b, a+1))
    
    return answer

print(solution(3, 5))
print(solution(3, 3))
print(solution(5, 3))