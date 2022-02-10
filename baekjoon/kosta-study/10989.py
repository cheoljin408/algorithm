import sys

N = int(sys.stdin.readline())

num_counts = [0 for _ in range(10000)]

for i in range(N):
    num = int(sys.stdin.readline())
    num_counts[num-1] += 1

for i in range(10000):
    if num_counts[i] != 0:
        for j in range(num_counts[i]):
            print(i+1)