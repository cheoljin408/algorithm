def solution(x):
    n = x
    sum = 0
    
    while n > 0:
        sum += n%10
        n = n//10
    
    if x%sum == 0:
        return True
    else:
        return False

print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))