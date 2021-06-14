import sys

class Stack:
    # INIT
    def __init__(self):
        self.top = []

    # IS EMPTY
    def isEmpty(self):
        if not self.top == []:
            return 0
        else:
            return 1

    # PUSH
    def push(self, item):
        self.top.append(item)

    # POP
    def pop(self):
        try:
            return self.top.pop()
        except IndexError:
            return -1

    # SIZE
    def size(self):
        return len(self.top)

    # TOP
    def checkTop(self):
        try:
            return self.top[-1]
        except IndexError:
            return -1

stack = Stack()

N = int(input())

for _ in range(N):
    option = sys.stdin.readline().split()

    if option[0] == 'push':
        stack.push(option[1])

    elif option[0] == 'pop':
        print(stack.pop())

    elif option[0] == 'size':
        print(stack.size())
    
    elif option[0] == 'empty':
        print(stack.isEmpty())
    
    elif option[0] == 'top':
        print(stack.checkTop())

print(stack.top)