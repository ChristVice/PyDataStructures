class Tree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add(self, child):
        child.parent = self
        self.children.append(child)

    def level(self):
        count = 0
        p = self.parent
        while p:
            count += 1
            p = p.parent

        return count

    def print(self):

        if self.level() == 0:
            prefix = ""
        else:
            dash = "|__"
            spaces = " " * self.level() * 4
            prefix = spaces + dash

        print(prefix, self.data)
        for child in self.children:
            child.print()


root = Tree("Electronics")

laptop = Tree("Laptop")
laptop.add(Tree("Toshiba"))
laptop.add(Tree("Dell"))
laptop.add(Tree("HP"))

phones = Tree("Phones")
phones.add(Tree("Apple"))
phones.add(Tree("Samsung"))
phones.add(Tree("Huawei"))

tv = Tree("TV")
tv.add(Tree("Samsung"))
tv.add(Tree("LG"))

root.add(laptop)
root.add(phones)
root.add(tv)

root.print()
