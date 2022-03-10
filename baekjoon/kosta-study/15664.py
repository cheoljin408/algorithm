import sys
import itertools

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

nums.sort()
c_nums = itertools.combinations(nums, M)

for i in sorted(list(set(c_nums))):
    for j in range(M):
        print(i[j], end=' ')
    print()