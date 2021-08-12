def solution(s):
    answer = ''
    list_s = list(s)
    k = 0
    
    for i in range(len(list_s)):
        if list_s[i] == ' ':
            k = -1
        if k%2 == 0:
            list_s[i] = list_s[i].upper()
            k += 1
        else:
            list_s[i] = list_s[i].lower()
            k += 1
        
    answer = ''.join(list_s)
    
    return answer

print(solution('try hello world'))