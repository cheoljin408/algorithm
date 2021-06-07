class Stack:
    # INIT
    def __init__(self):
        self.top = []

    # IS EMPTY
    def isEmpty(self):
        if not self.top == []:
            return 1
        else:
            return 0

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
    def top(self):
        try:
            return self.top[-1]
        except IndexError:
            return -1