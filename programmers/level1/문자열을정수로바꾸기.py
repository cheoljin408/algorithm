def solution(s):
    s = list(s)
    sign = ''
    answer = 0

    if s[0] == '+' or s[0] == '-':
        sign = s.pop(0)

    if sign == '-':
        x = len(s) - 1
        for i in range(len(s)):
            answer -= int(s[i]) * (10**x)
            x -= 1
    else:
        x = len(s) - 1
        for i in range(len(s)):
            answer += int(s[i]) * (10**x)
            x -= 1

    return answer

print(solution("1234"))
print(solution("-1234"))