from binarytree import BinarySearchTree


class AbstractSet:
    def union(self, other_set):
        """ Makes a union with the other set and returns a new set 
            Time complexity: O(n^2) for the 2 for loops on different sets
                    O(logN) Based off contains method and O(1) for add"""
        new_set = TreeSet()
        for item in self:
            if item not in new_set:
                new_set.add(item)
        for item in other_set:
            if item not in new_set:
                new_set.add(item)
        return new_set


    def intersection(self, other_set):
        """ Makes an intersection between self and other set
            Time complexity: O(n) for looping through initial items
                    O(logN) Based off contains method and O(1) for add"""
        new_set = TreeSet()
        for item in self:
            if other_set.contains(item):
                new_set.add(item)
        return new_set


    def difference(self, other_set):
        """ Gets the difference between two sets and returns it.
            Time complexity: O(n^2) for the 2 for loops on different sets
                    O(logN) Based off contains method and O(1) for add"""
        new_set = TreeSet()
        for item in self:
            if not other_set.contains(item) and item not in new_set:
                new_set.add(item)
        for item in other_set:
            if not self.contains(item) and item not in new_set:
                new_set.add(item)
        return new_set


    def is_subset(self, items):
        """ Checks if all the items in other_set are in self
            Time complexity:  O(n) for looping through initial items
                    O(logN) Based off contains method"""
        for item in items:
            if not self.contains(item):
                return False
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
        """ Makes size an attribute """
        return self.tree.size


    @property
    def is_empty(self):
        """ Checks if the set is empty
            Time complexity: O(1) checks if there is a root present"""
        return self.tree.is_empty()


    def __iter__(self):
        for item in self.items():
            yield item


    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'Set({!r})'.format(self.tree.items_in_order())


    def contains(self, item):
        """ Checks if item is in the set
            Time Complexity: O(logN) only grows in relation to the #node vs height
            starts fast/heavy then peeks with a lot for a long time"""
        return self.tree.contains(item)


    def add(self, item):
        """ Insert one item to the set if it doesn't already exist 
            Time complexity: O(logN) based off contains then just O(1) to add"""
        if not self.contains(item):
            self.tree.insert(item)

    def remove(self, item):
        """ Check if item exists and remove it or raise Keyerror
            Time complexity: O() """
        if self.contains(item):
            self.tree.delete(item)
        else:
            raise ValueError(item, "Is not in this set")

    def items(self):
        return self.tree.items_in_order()


