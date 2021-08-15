def solution(s):
    s = list(s.upper())
    
    pCount = s.count('P')
    yCount = s.count('Y')
    
    return True if pCount == yCount else False

print(solution("pPoooyY"))
print(solution("Pyy"))