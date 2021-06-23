from collections import deque
import sys

def empty(x):
    if len(x) == 0:
        return 1
    return 0

N = int(sys.stdin.readline())
arr = deque()

for _ in range(N):
    option = list(sys.stdin.readline().split())

    if option[0] == 'push_front':
        arr.appendleft(option[1])
    elif option[0] == 'push_back':
        arr.append(option[1])
    elif option[0] == 'pop_front':
        if empty(arr) == 1:
            print(-1)
        else:
            print(arr.popleft())
    elif option[0] == 'pop_back':
        if empty(arr) == 1:
            print(-1)
        else:
            print(arr.pop())
    elif option[0] == 'size':
        print(len(arr))
    elif option[0] == 'empty':
        print(empty(arr))
    elif option[0] == 'front':
        if empty(arr) == 1:
            print(-1)
        else:
            print(arr[0])
    elif option[0] == 'back':
        if empty(arr) == 1:
            print(-1)
        else:    
            print(arr[len(arr)-1])