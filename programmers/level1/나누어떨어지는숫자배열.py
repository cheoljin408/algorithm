def solution(arr, divisor):
    answer = []
    
    for i in arr:
        if i%divisor == 0:
            answer.append(i)
    answer.sort()
    
    return [-1] if len(answer) == 0 else answer

print(solution([5, 9, 7, 10], 5))
print(solution([2, 36, 1, 3], 1))
print(solution([3,2,6], 10))