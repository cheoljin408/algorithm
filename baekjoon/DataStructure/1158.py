N, K = map(int, input().split())
nums = []
idx = 0
answer = []

for i in range(1, N+1):
    nums.append(i)

for _ in range(N):
    idx += K-1
    if idx >= len(nums):
        idx = idx % len(nums)
    answer.append(nums.pop(idx))

print('<' + ','.join(map(str, answer)) + '>')