# import sys
# 
# N = int(sys.stdin.readline())
# nums = list(map(int, sys.stdin.readline().split()))
# idx_list = []
# for i in range(1, N+1):
#     idx_list.append(i)
# result = []
# 
# idx = 0
# num = nums.pop(idx)
# result.append(idx_list.pop(idx))
# 
# while nums:
#     if num > 0:
#         idx = (idx + (num - 1)) % len(nums)
#     else:
#         idx = (idx + num) % len(nums)
#     num = nums.pop(idx)
#     result.append(idx_list.pop(idx))
# 
# for i in result:
#     print(i, end=' ')
#     
import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
idx_list = []
for i in range(1, N+1):
    idx_list.append(i)
result = []

idx = 0
num = nums.pop(idx)
result.append(idx_list.pop(idx))

while nums:
    if num > 0:
        idx = (idx + (num - 1)) % len(nums)
    else:
        idx = (idx + num) % len(nums)
    num = nums.pop(idx)
    result.append(idx_list.pop(idx))

for i in result:
    print(i, end=' ')