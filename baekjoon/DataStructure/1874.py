# import sys
#
# N = int(sys.stdin.readline())
# nums = []
# plus_num = 0
# stck = []
# answer = []
# flag = True
#
# for i in range(N):
#     nums.append(int(sys.stdin.readline()))
#
# for i in nums:
#     while True:
#         if i <= plus_num:
#             break
#         plus_num += 1
#         stck.append(plus_num)
#         answer.append('+')
#     # print(stck)
#     # print(answer)
#
#     if i == stck[-1]:
#         stck.pop()
#         answer.append('-')
#
#     else:
#         flag = False
#
# if not flag:
#     print('NO')
# else:
#     print('\n'.join(answer))

import sys

num_list = []

N = int(sys.stdin.readline())
for _ in range(N):
    num_list.append(int(sys.stdin.readline()))

count = 0
stack = []
answer = []
flag = True
for num in num_list:
    while True:
        if num == count:
            break
        count += 1
        stack.append(count)
        answer.append('+')

    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        flag = False

if not flag:
    print('NO')
else:
    for a in answer:
        print(a)

