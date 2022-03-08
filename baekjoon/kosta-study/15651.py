import itertools
import sys

N, M = map(int, sys.stdin.readline().split())

nums = itertools.product(range(1, N+1), repeat=M)

for i in nums:
    for j in range(M):
        print(i[j], end=' ')
    print()