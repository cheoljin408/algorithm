# N, K = map(int, input().split())
# nums = []
# idx = 0
# answer = []
#
# for i in range(1, N+1):
#     nums.append(i)
#
# for _ in range(N):
#     idx += K-1
#     if idx >= len(nums):
#         idx = idx % len(nums)
#     answer.append(nums.pop(idx))
#
# print('<' + ','.join(map(str, answer)) + '>')

N, K = map(int, input().split())
answer = []
nums = [i for i in range(1, N+1)]
idx = K-1
while True:
    num = nums.pop(idx)
    answer.append(num)
    if len(nums) == 0:
        break
    idx += K - 1
    if idx >= len(nums):
        idx = idx%len(nums)

print('<' + ', '.join(map(str, answer)) + '>')
