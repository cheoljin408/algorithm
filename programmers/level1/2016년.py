import sys

def solution(a, b):
    answer = ''
    day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    date = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    sum = 0
    idx = 0

    for i in range(a-1):
        sum += date[i]
    sum += b

    idx = sum % 7
    answer = day[idx]

    return answer

m, d = list(map(int, sys.stdin.readline().split()))
result = solution(m, d)
print(result)