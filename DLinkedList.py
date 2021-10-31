class Node:
    def __init__(self, val):
        self.prev = None
        self.val = val
        self.next = None


class DLinkedList:
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
            while n.next is not None:
                n = n.next

            n.next = node
            node.prev = n
            self.tail = node

    def insert(self, index, item):
        node = Node(item)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            n = self.head
            for i in range(index):
                if n.next is None and i < index:
                    print("Index out of bounds")
                    return
                if n.next is not None:
                    n = n.next

            n.prev.next = node
            node.next = n
            node.prev = n.prev
            n.prev = node

    def remove(self, item):
        if self.head is None:
            print("No items in list")
            return

        if self.head.next is None:
            if self.head.val is item:
                self.head = None
                self.tail = None
            else:
                print("No items in list")
                return
        else:
            if self.head.val is item:
                self.head = self.head.next
                self.head.prev = None

        n = self.head
        while n.next is not None:
            if n.val is item:
                break
            n = n.next

        if n.next is not None:
            n.prev.next = n.next
            n.next.prev = n.prev
        else:
            if n.val is item:
                self.tail = n.prev
                n.prev.next = None
            else:
                print("No items in list")

    def get_head(self):
        if self.head is None:
            print("Noe items in list")
            return

        return self.head

    def get_tail(self):
        if self.tail is None:
            print("No items in list")
            return

        return self.tail

    def get(self, item):
        if self.head is None:
            return

        n = self.head
        while n:
            if n.val is item:
                return n
            n = n.next

        print("Item does not exits")

    def reverse(self):
        if self.head is None:
            return

        p = self.head
        q = self.head.next
        p.next = None
        p.prev = q
        while q:
            q.prev = q.next
            q.next = p
            p = q
            q = q.prev

        self.head = p

    def print(self):
        if self.head is None:
            print("Nothing in list")
            return

        n = self.head
        while n is not None:
            print(n.val, end=", ")
            n = n.next

        print(end="\n")

    def __len__(self):
        if self.head is None:
            print("Nothing in list")
            return

        count = 0
        n = self.head
        while n is not None:
            count += 1
            n = n.next

        return count


l = DLinkedList()

for i in range(1, 11):
    l.append(i)

l.print()
l.insert(2, 90)
l.print()
