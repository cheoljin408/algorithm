def solution(n):
    answer = 0

    for i in list(str(n)):
        answer += int(i)

    return answer

print(solution(123))
print(solution(987))