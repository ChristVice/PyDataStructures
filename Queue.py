class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            self.tail = node

    def empty(self):
        return self.head == None

    def peek(self):
        return self.head.value

    def remove(self):
        if self.head is None:
            return

        data = self.head.value

        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

        return data

    def __len__(self):
        count = 0
        if self.head is None:
            return count

        n = self.head
        while n:
            count += 1
            n = n.next

        return count

    def print(self):
        if self.head is None:
            return

        n = self.head
        while n:
            print(n.value, end=", ")
            n = n.next

        print(end="\n")


l = Queue()

for i in range(1, 11):
    l.add(i)

print(len(l))
l.print()
print(l.peek())
print(l.remove())
l.print()