import sys

N = int(sys.stdin.readline())

xy = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

xy.sort(key=lambda x: (x[1], x[0]))

for i in xy:
    print(i[0], i[1])