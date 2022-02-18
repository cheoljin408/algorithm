# import sys
#
# string = list(sys.stdin.readline())
# sum = 0
# cut_left = 0
# cut_right = 1
#
# for idx, item in enumerate(string):
#     if item == '(':
#         cut_left += 1
#     elif item == ')':
#         cut_left -= 1
#         if string[idx-1] == '(':
#             sum += cut_left
#         else:
#             sum += cut_right
#
# print(sum)

import sys

stick = list(sys.stdin.readline())
stick.pop()
sum = 0
left = 0
right = 1
for i, e in enumerate(stick):
    if e == '(':
        left += 1
    else:
        left -= 1
        if stick[i-1] == '(':
            sum += left
        else:
            sum += right

print(sum)

