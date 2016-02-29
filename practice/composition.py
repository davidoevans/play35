"""
Why do we care?

Because composition and object construction is what objects are all about. Objects are composed of stuff and
they need to be initialised somehow. This also ties up some stuff about recursion and use of generators.

Generators are great. You could have achieved similar functionality to print_all_2 by just constructing a big
long list and then printing it's contents. One of the nice things about generators is that they don't need to
take up much space in memory.

It is also worth pointing out that print_all_1 traverses the tree in a depth-first manner, while print_all_2
is width-first. Make sure you understand those terms. Sometimes one kind of traversal is more appropriate than
the other. But that depends very much on your application.
"""


class Node(object):
    def __init__(self, s_name):
        self._l_children = []
        self.sName = s_name

    def __repr__(self):
        return "<Node '{}'>".format(self.sName)

    def append(self, *args, **kwargs):
        self._l_children.append(*args, **kwargs)

    def print_all_1(self):
        print(self)
        for oChild in self._l_children:
            oChild.print_all_1()

    def print_all_2(self):
        def gen(o):
            l_all = [o, ]
            while l_all:
                o_next = l_all.pop(0)
                l_all.extend(o_next._l_children)
                yield o_next

        for o_node in gen(self):
            print(o_node)


oRoot = Node("root")
oChild1 = Node("child1")
oChild2 = Node("child2")
oChild3 = Node("child3")
oChild4 = Node("child4")
oChild5 = Node("child5")
oChild6 = Node("child6")
oChild7 = Node("child7")
oChild8 = Node("child8")
oChild9 = Node("child9")
oChild10 = Node("child10")

oRoot.append(oChild1)
oRoot.append(oChild2)
oRoot.append(oChild3)
oChild1.append(oChild4)
oChild1.append(oChild5)
oChild2.append(oChild6)
oChild4.append(oChild7)
oChild3.append(oChild8)
oChild3.append(oChild9)
oChild6.append(oChild10)

# specify output from here onwards

print("Depth first")
oRoot.print_all_1()
print("Width first")
oRoot.print_all_2()
