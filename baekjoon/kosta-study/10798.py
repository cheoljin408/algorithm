import sys


answer = [[0] * 15 for i in range(5)]

for i in range(5):
    s = list(sys.stdin.readline())
    s.pop()
    for j in range(len(s)):
        answer[i][j] = s[j]

result = []
for i in range(15):
    for j in range(5):
        if answer[j][i] == 0:
            continue
        else:
            result.append(answer[j][i])

print(''.join(result))