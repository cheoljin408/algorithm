# import sys
#
# class Stack:
#     # INIT
#     def __init__(self):
#         self.top = []
#
#     # IS EMPTY
#     def isEmpty(self):
#         if not self.top == []:
#             return 0
#         else:
#             return 1
#
#     # PUSH
#     def push(self, item):
#         self.top.append(item)
#
#     # POP
#     def pop(self):
#         try:
#             return self.top.pop()
#         except IndexError:
#             return -1
#
#     # SIZE
#     def size(self):
#         return len(self.top)
#
#     # TOP
#     def checkTop(self):
#         try:
#             return self.top[-1]
#         except IndexError:
#             return -1
#
# stack = Stack()
#
# N = int(input())
#
# for _ in range(N):
#     option = sys.stdin.readline().split()
#
#     if option[0] == 'push':
#         stack.push(option[1])
#
#     elif option[0] == 'pop':
#         print(stack.pop())
#
#     elif option[0] == 'size':
#         print(stack.size())
#
#     elif option[0] == 'empty':
#         print(stack.isEmpty())
#
#     elif option[0] == 'top':
#         print(stack.checkTop())
#
# print(stack.top)

import sys

def push(stack, item):
    stack.append(item)

def pop(stack):
    if len(stack) == 0:
        print(-1)
        return
    print(stack.pop())

def size(stack):
    print(len(stack))

def empty(stack):
    if len(stack) == 0:
        print(1)
        return
    print(0)

def top(stack):
    if len(stack) == 0:
        print(-1)
        return
    print(stack[len(stack)-1])

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    operation = sys.stdin.readline().split()

    if operation[0] == 'push':
        push(stack, operation[1])
    elif operation[0] == 'pop':
        pop(stack)
    elif operation[0] == 'size':
        size(stack)
    elif operation[0] == 'empty':
        empty(stack)
    elif operation[0] == 'top':
        top(stack)


