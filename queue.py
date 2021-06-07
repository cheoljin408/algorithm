class Queue:
    # INIT
    def __init__(self):
        self.queue = []

    # IS EMPTY
    def isEmpty(self):
        if not self.queue == []:
            return 0
        else:
            return 1

    # PUSH
    def push(self, item):
        self.queue.insert(0, item)

    # POP
    def pop(self):
        try:
            return self.queue.pop()
        except IndexError:
            return -1

    # SIZE
    def size(self):
        return len(self.queue)

    # FRONT
    def front(self):
        try:
            return self.queue[-1]
        except IndexError:
            return -1

    # BACK
    def back(self):
        try:
            return self.queue[0]
        except IndexError:
            return -1