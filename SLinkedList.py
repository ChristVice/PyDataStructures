class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, item):
        node = Node(item)

        if self.head is None:
            self.head = node
            self.tail = node

        else:
            n = self.head
            while n.next:
                n = n.next

            n.next = node
            self.tail = node

    def remove(self, item):
        if self.head is None:
            return

        if self.head.value == item and self.head.next is None:
            self.head = None
            self.tail = None
            return

        if self.head.value == item:
            self.head = self.head.next
            return

        n = self.head
        while n.next:
            if n.next.value == item:
                break
            n = n.next

        if n.next is None:
            return
        else:
            if n.next is self.tail:
                self.tail = n
            n.next = n.next.next

    def remove_index(self, index):

        if self.head is None:
            return

        if index == 0:
            if self.head.next is None:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next

        n = self.head
        for i in range(index - 1):
            if n.next is None and i < index:
                print("index out of bounds")
                return
            n = n.next

        n.next = n.next.next

    def reverse(self):

        if self.head is None:
            return

        prev = None
        n = self.head
        while n:
            nxt = n.next
            n.next = prev
            prev = n
            n = nxt

        self.head = prev

    def print(self):
        if self.head is None:
            return

        n = self.head
        while n:
            print(n.value, end=", ")
            n = n.next

        print(end="\n")

    def __len__(self):
        count = 0

        if self.head is None:
            return count

        n = self.head
        while n:
            count += 1
            n = n.next

        return count


l = SLinkedList()

for i in range(1, 21):
    l.append(i)

l.print()
print(l.tail.value)
l.remove(20)
l.print()
print(l.tail.value)
