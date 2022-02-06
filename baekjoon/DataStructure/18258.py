# import sys
#
# class Queue:
#     # INIT
#     def __init__(self):
#         self.queue = []
#         self.idx = 0
#
#     # IS EMPTY
#     def isEmpty(self):
#         if len(self.queue) == self.idx:
#             self.idx = 0
#             self.queue = []
#             return 1
#         else:
#             return 0
#
#     # PUSH
#     def push(self, item):
#         self.queue.append(item)
#         print(self.queue)
#
#     # POP
#     def pop(self):
#         if len(self.queue) > self.idx:
#             self.idx += 1
#             return(self.queue[self.idx - 1])
#         else:
#             return -1
#
#     # SIZE
#     def size(self):
#         return len(self.queue) - self.idx
#
#     # FRONT
#     def front(self):
#         if len(self.queue) > self.idx:
#             return self.queue[self.idx]
#         else:
#             return -1
#
#     # BACK
#     def back(self):
#         if len(self.queue) > self.idx:
#             return self.queue[-1]
#         else:
#             return -1
#
# queue = Queue()
# N = int(input())
#
# for _ in range(N):
#     option = sys.stdin.readline().split()
#
#     if option[0] == 'push':
#         queue.push(option[1])
#
#     elif option[0] == 'pop':
#         print(queue.pop())
#
#     elif option[0] == 'size':
#         print(queue.size())
#
#     elif option[0] == 'empty':
#         print(queue.isEmpty())
#
#     elif option[0] == 'front':
#         print(queue.front())
#
#     elif option[0] == 'back':
#         print(queue.back())

import sys

def push(queue, item):
    queue.append(item)

def pop(queue, front_idx):
    if len(queue) <= front_idx:
        print(-1)
        return
    print(queue[front_idx])

def size(queue, front_idx):
    print(len(queue)-front_idx)

def empty(queue, front_idx):
    if len(queue) == front_idx:
        print(1)
        return
    print(0)

def front(queue, front_idx):
    if len(queue) == front_idx:
        print(-1)
        return
    print(queue[front_idx])

def back(queue, front_idx):
    if len(queue) == front_idx:
        print(-1)
        return
    print(queue[len(queue)-1])


N = int(sys.stdin.readline())
front_idx = 0
queue = []

for _ in range(N):
    operation = sys.stdin.readline().split()

    if operation[0] == 'push':
        push(queue, operation[1])

    elif operation[0] == 'pop':
        pop(queue, front_idx)
        if len(queue) > front_idx:
            front_idx += 1

    elif operation[0] == 'size':
        size(queue, front_idx)

    elif operation[0] == 'empty':
        empty(queue, front_idx)

    elif operation[0] == 'front':
        front(queue, front_idx)

    elif operation[0] == 'back':
        back(queue, front_idx)
