class BinarySearchTree:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def append(self, item):
        if self.value is None:
            self.value = item
        else:
            self._append(item)

    def _append(self, item):
        if self.value is item:
            return

        if item < self.value:
            if self.left:
                self.left._append(item)
            else:
                self.left = BinarySearchTree(item)

        else:
            if self.right:
                self.right._append(item)
            else:
                self.right = BinarySearchTree(item)

    def min_value(self):
        if self.left is None:
            return self.value

        return self.left.min_val()

    def max_value(self):
        if self.right is None:
            return self.value

        return self.right.max_value()

    def delete(self, value):
        if value < self.value:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.value:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val = self.right.min_value()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

    def print(self):
        if self.left:
            self.left.print()

        print(self.value, end=", ")

        if self.right:
            self.right.print()

    def preorder(self):
        print(self.value, end=", ")
        if self.left:
            self.left.print()
        if self.right:
            self.right.print()


def dfs(root):
    stack = [root]

    while len(stack) > 0:
        curr = stack.pop()
        print(curr.value, end=", ")

        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)

    print(end="\n")


from collections import deque


def bfs(root):
    queue = deque()
    queue.append(root)

    while len(queue) > 0:
        curr = queue.popleft()
        print(curr.value, end=". ")

        if curr.left:
            queue.append(curr.left)

        if curr.right:
            queue.append(curr.right)

    print(end="\n")


root = BinarySearchTree()

l = []
for i in range(1, 11):
    l.append(i)

import random

random.shuffle(l)


for i in l:
    root.append(i)

root.print()
print(end="\n")

print("dfs")
dfs(root)
print("bfs")
bfs(root)
root.preorder()
