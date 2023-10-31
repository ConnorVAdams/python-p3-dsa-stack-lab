class Stack:
    
    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            print('Stack is full, cannot push.')

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            print('Stack is empty, cannot pop.')

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            print('Stack is empty, cannot peek.')
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        if target in self.items:
            return len(self.items) - (self.items.index(target) + 1)
        else:
            return -1
