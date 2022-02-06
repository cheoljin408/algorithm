# import sys
# from collections import deque
#
# N = int(sys.stdin.readline())
#
# queue = deque(i+1 for i in range(N))
#
# while(len(queue) > 1):
#     queue.popleft()
#     tmp = queue.popleft()
#     queue.append(tmp)
#
# print(queue[0])

import sys
from collections import deque

N = int(sys.stdin.readline())

stack = deque(i for i in range(1, N+1))


while True:
    if len(stack) == 1:
        break

    stack.popleft()
    if len(stack) == 1:
        break

    num = stack.popleft()
    stack.append(num)

print(stack[0])