# from collections import deque
# import sys
#
# def empty(x):
#     if len(x) == 0:
#         return 1
#     return 0
#
# N = int(sys.stdin.readline())
# arr = deque()
#
# for _ in range(N):
#     option = list(sys.stdin.readline().split())
#
#     if option[0] == 'push_front':
#         arr.appendleft(option[1])
#     elif option[0] == 'push_back':
#         arr.append(option[1])
#     elif option[0] == 'pop_front':
#         if empty(arr) == 1:
#             print(-1)
#         else:
#             print(arr.popleft())
#     elif option[0] == 'pop_back':
#         if empty(arr) == 1:
#             print(-1)
#         else:
#             print(arr.pop())
#     elif option[0] == 'size':
#         print(len(arr))
#     elif option[0] == 'empty':
#         print(empty(arr))
#     elif option[0] == 'front':
#         if empty(arr) == 1:
#             print(-1)
#         else:
#             print(arr[0])
#     elif option[0] == 'back':
#         if empty(arr) == 1:
#             print(-1)
#         else:
#             print(arr[len(arr)-1])

import sys
import collections

def push_front(deq, item):
    deq.appendleft(item)

def push_back(deq, item):
    deq.append(item)

def pop_front(deq):
    if len(deq) == 0:
        print(-1)
        return
    print(deq.popleft())

def pop_back(deq):
    if len(deq) == 0:
        print(-1)
        return
    print(deq.pop())

def size(deq):
    print(len(deq))

def empty(deq):
    if len(deq) == 0:
        print(1)
        return
    print(0)

def front(deq):
    if len(deq) == 0:
        print(-1)
        return
    print(deq[0])

def back(deq):
    if len(deq) == 0:
        print(-1)
        return
    print(deq[-1])


N = int(sys.stdin.readline())
deq = collections.deque()

for _ in range(N):
    operation = sys.stdin.readline().split()

    if operation[0] == 'push_front':
        push_front(deq, operation[1])
    elif operation[0] == 'push_back':
        push_back(deq, operation[1])
    elif operation[0] == 'pop_front':
        pop_front(deq)
    elif operation[0] == 'pop_back':
        pop_back(deq)
    elif operation[0] == 'size':
        size(deq)
    elif operation[0] == 'empty':
        empty(deq)
    elif operation[0] == 'front':
        front(deq)
    elif operation[0] == 'back':
        back(deq)



