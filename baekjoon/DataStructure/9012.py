# N = int(input())
#
# for _ in range(N):
#     stck = []
#     check = True
#     string = input()
#
#     for i in string:
#         if i == '(':
#             stck.append('(')
#         elif i == ')':
#             if len(stck) == 0:
#                 check = False
#             else:
#                 stck.pop(-1)
#
#     if check == False or len(stck) != 0:
#         print('NO')
#     else:
#         print('YES')
#
#
#

import sys

N = int(sys.stdin.readline())

for _ in range(N):
    string = sys.stdin.readline()

    stack = []
    sum = 0
    answer = True

    for item in string:
        if item == '(':
            sum += 1
            stack.append('(')

        elif item == ')':
            sum -= 1
            if len(stack) > 0:
                stack.pop()

    if len(stack) != 0 or sum != 0:
        answer = False

    if answer:
        print('YES')
    else:
        print('NO')