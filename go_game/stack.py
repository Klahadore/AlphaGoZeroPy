class Stack():
    def __init__(self):
        self.container = []

    def is_empty(self) -> int:
        return len(self.container) == 0

    def push (self, item):
        self.container.append(item)
        return item

    def pop(self):
        if self.is_empty():
            raise Exception("empty stack, can't pop from")
        return self.container.pop()

    def size(self):
        return len(self.container)

    def show(self):
        return self.container
