def solution(s, n):
    s = list(s)
    
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((((ord(s[i]) + n)-65)%26)+65)
        elif s[i].islower():
            s[i] = chr((((ord(s[i]) + n)-97)%26)+97)
    
    return ''.join(s)

print(solution('AB', 1))
print(solution('z', 1))
print(solution('a B z', 4))