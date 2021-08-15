def solution(strings, n):
    strings.sort()
    answer = []
    idx = [i for i in range(len(strings))]
    chars = []
    
    for s in strings:
        chars.append(list(s)[n])
    
    for i in range(len(chars)):
        for j in range(0, len(chars) - i - 1):
            if chars[j] > chars[j+1]:
                chars[j], chars[j+1] = chars[j+1], chars[j]
                idx[j], idx[j+1] = idx[j+1], idx[j]        
                
    for i in idx:
        answer.append(strings[i])
        
    return answer

print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))