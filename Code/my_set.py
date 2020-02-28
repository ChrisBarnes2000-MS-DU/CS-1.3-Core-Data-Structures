from binarytree import BinarySearchTree


class AbstractSet:
    def union(self, other_set):
        pass

    def intersection(self, other_set):
        new_set = TreeSet()
        for item in self.items():
            if other_set.contains(item):
                new_set.add(item)
        return new_set

    def difference(self):
        pass

    def is_subset(self, items):
        for item in items:
            if self.contains(item):
                continue
            else:
                raise ValueError(item, "Is not in this set")


class TreeSet(AbstractSet):
    def __init__(self, elements=None):
        """Initialize this binary tree node with the given data."""
        self.tree = BinarySearchTree()
        if elements is not None:
            for element in elements:
                self.add(element)

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
            self.tree.remove(item)
        else:
            raise ValueError(item, "Is not in this set")

    def items(self):
        return self.tree.items_in_order()

def test_Set():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    items = [4, 2, 6, 1, 3, 5, 7]
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: {}'.format(items))

    # my_set = Set(items)
    # print(my_set)
    # print(my_set.contains(items[3]))

    # print('\nInserting items:')
    # for item in items:
    #     tree.insert(item)
    #     print('insert({}), size: {}'.format(item, tree.size))
    # print('root: {}'.format(tree.root))

    # print('\nSearching for items:')
    # for item in items:
    #     result = tree.search(item)
    #     print('search({}): {}'.format(item, result))
    # item = 123
    # result = tree.search(item)
    # print('search({}): {}'.format(item, result))

    # print('\nTraversing items:')
    # print('items in-order:    {}'.format(tree.items_in_order()))
    # print('items pre-order:   {}'.format(tree.items_pre_order()))
    # print('items post-order:  {}'.format(tree.items_post_order()))
    # print('items level-order: {}'.format(tree.items_level_order()))


if __name__ == '__main__':
    test_Set()
