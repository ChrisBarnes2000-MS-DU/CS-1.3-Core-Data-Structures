from binarytree import BinarySearchTree


class AbstractSet:
    def union(self, other_set):
        new_set = TreeSet()
        for item in self:
            if item not in new_set:
                new_set.add(item)
        for item in other_set:
            if item not in new_set:
                new_set.add(item)
        return new_set


    def intersection(self, other_set):
        new_set = TreeSet()
        for item in self.items():
            if other_set.contains(item):
                new_set.add(item)
        return new_set


    # def difference(self):
    #     new_set = TreeSet()
    #     for item in self.items():
    #         if other_set.contains(item):
    #             new_set.add(item)
    #     return new_set


    def is_subset(self, items):
        for item in items:
            if not self.contains(item):
                return False
            #     raise ValueError(item, "Is not in this set")
        return True




class TreeSet(AbstractSet):
    def __init__(self, elements=None):
        """Initialize this binary tree node with the given data."""
        self.tree = BinarySearchTree()
        if elements is not None:
            for element in elements:
                self.add(element)


    @property
    def size(self):
        return self.tree.size


    def __iter__(self):
        for item in self.items():
            yield item


    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'Set({!r})'.format(self.tree.items_in_order())


    def is_empty(self):
        return self.tree.is_empty()


    def contains(self, item):
        return self.tree.contains(item)


    def add(self, item):
        if not self.contains(item):
            self.tree.insert(item)

    def remove(self, item):
        if self.contains(item):
            self.tree.delete(self.tree.root, item)
        else:
            raise ValueError(item, "Is not in this set")

    def items(self):
        return self.tree.items_in_order()


