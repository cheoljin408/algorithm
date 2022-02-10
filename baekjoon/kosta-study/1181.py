import sys

N = int(sys.stdin.readline())
strs = [input() for i in range(N)]

strs = list(set(strs))
strs.sort(key=lambda x: (len(x), x))

for i in range(len(strs)):
    print(strs[i])