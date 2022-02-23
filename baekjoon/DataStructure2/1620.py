# import sys
#
# N, M = map(int, sys.stdin.readline().split())
# names = {}
# indexes = {}
#
# for i in range(1, N+1):
#     name = sys.stdin.readline().strip()
#     names[i] = name
#     indexes[name] = i
#
# for i in range(M):
#     option = sys.stdin.readline().strip()
#     if option.isdigit():
#         print(names[int(option)])
#     else:
#         print(indexes[option])

import sys

N, M = map(int, sys.stdin.readline().split())
names = {}
indexes = {}

for i in range(1, N+1):
    name = sys.stdin.readline().strip()
    names[i] = name
    indexes[name] = i

for i in range(M):
    option = sys.stdin.readline().strip()
    if option.isdigit():
        print(names[int(option)])
    else:
        print(indexes[option])