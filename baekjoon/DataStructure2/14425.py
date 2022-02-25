# import sys
#
# N, M = map(int, sys.stdin.readline().split())
# strings = {}
# cnt = 0
#
# for _ in range(N):
#     string = sys.stdin.readline().strip()
#     strings[string] = True
#
# for _ in range(M):
#     option = sys.stdin.readline().strip()
#     if option in strings:
#         cnt += 1
#
# print(cnt)

import sys

N, M = map(int, sys.stdin.readline().split())
strings = {}
cnt = 0

for _ in range(N):
    string = sys.stdin.readline().strip()
    strings[string] = True

for _ in range(M):
    option = sys.stdin.readline().strip()
    if option in strings:
        cnt += 1

print(cnt)