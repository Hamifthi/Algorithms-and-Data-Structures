class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.queue.pop()

    def is_empty(self):
        return len(self.queue) == 0