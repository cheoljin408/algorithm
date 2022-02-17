# import sys
#
# N = int(sys.stdin.readline())
# string = list(sys.stdin.readline())
# nums = []
# for _ in range(N):
#     nums.append(int(sys.stdin.readline()))
#
# for idx, val in enumerate(string):
#     if val >= 'A' and val <= 'Z':
#         string[idx] = nums[ord(val) - ord('A')]
#
# len_string = len(string)
#
# stck = []
#
# for i in string[:len_string-1]:
#     if i == '+':
#         num1 = stck.pop()
#         num2 = stck.pop()
#         stck.append(num2 + num1)
#     elif i == '-':
#         num1 = stck.pop()
#         num2 = stck.pop()
#         stck.append(num2 - num1)
#     elif i == '*':
#         num1 = stck.pop()
#         num2 = stck.pop()
#         stck.append(num2 * num1)
#     elif i == '/':
#         num1 = stck.pop()
#         num2 = stck.pop()
#         stck.append(num2 / num1)
#     else:
#         stck.append(i)
#
# print("%.2f" % (stck[0]))

import sys

N = int(sys.stdin.readline())
formula = list(sys.stdin.readline())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline()))

idx = 0
for i in range(len(formula)):
    if formula[i].isalpha():
        formula[i] = nums[ord(formula[i]) - ord('A')]

formula.pop()
stack = []
for char in formula:
    if isinstance(char, int):
        stack.append(char)
    elif char == '+':
        num1 = stack.pop()
        num2 = stack.pop()
        stack.append(num2 + num1)
    elif char == '-':
        num1 = stack.pop()
        num2 = stack.pop()
        stack.append(num2 - num1)
    elif char == '*':
        num1 = stack.pop()
        num2 = stack.pop()
        stack.append(num2 * num1)
    elif char == '/':
        num1 = stack.pop()
        num2 = stack.pop()
        stack.append(num2 / num1)
print("%.2f" % (stack[0]))