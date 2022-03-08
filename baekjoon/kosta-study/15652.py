import itertools
import sys

N, M = map(int, sys.stdin.readline().split())

nums = itertools.combinations_with_replacement(range(1, N+1), M)

for i in nums:
    for j in range(M):
        print(i[j], end=' ')
    print()