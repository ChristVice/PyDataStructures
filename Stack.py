class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def peek(self):
        if len(self.stack) == 0:
            return

        return self.stack[-1]

    def pop(self):
        if len(self.stack) == 0:
            return

        data = self.stack[-1]
        del self.stack[-1]
        return data

    def print(self):
        for i in self.stack:
            print(i, end=", ")

        print(end="\n")


l = Stack()


for i in range(1, 11):
    l.push(i)

l.print()
print(l.peek())
l.pop()
l.print()
print(l.peek())