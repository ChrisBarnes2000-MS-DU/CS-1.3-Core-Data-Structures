from binarytree import BinarySearchTree
from hashtable import HashTable


class AbstractSet:
    def __iter__(self):
        for item in self.items():
            yield item


    def union(self, other_set):
        """ Makes a union with the other set and returns a new set 
            Time complexity: O(m+n log(m+n)) same for both
                    O(n) for looping through initial items
                    O(logn) Based off contains method and O(1) for add"""
        new_set = TreeSet(self)     # O(m)
        for item in other_set:      # O(n)
            new_set.add(item)       # O(log (m + n))
        return new_set              # O(m+n log(m+n))


    def intersection(self, other_set):
        """ Makes an intersection between self and other set
            Time complexity: O(mlogn)
                    O(m) for looping through initial items
                    O(log n) Based off contains method and O(log min(m,n)) for add"""
        new_set = TreeSet()
        # new_set = HashSet()
        if self.size < other_set.size:
            for item in self:                   # m 
                if other_set.contains(item):    #log n
                    new_set.add(item)           #log of [new_set <= min(m, n) ]
            return new_set


    def difference(self, other_set):
        """ Gets the difference between two sets and returns it.
            Time complexity: O(mlogm) + O(nlogn) same for both
                    O(n) for looping through initial items
                    O(logn) Based off contains method and O(1) for add"""
        new_set = TreeSet()
        for item in self:
            if not other_set.contains(item):
                new_set.add(item)
        for item in other_set:
            if not self.contains(item):
                new_set.add(item)
        return new_set


    def is_subset(self, items):
        """ Checks if all the items in other_set are in self
            Time complexity:  O(nlogn) 
                    O(n) for looping through initial items
                    O(logn) Based off contains method"""
        for item in items:
            if not self.contains(item):
                return False
        return True


    @property
    def is_empty(self):
        """ Checks if the set is empty
            Time complexity: O(1) checks if there is a root present"""
        return self.size == 0







class TreeSet(AbstractSet):
    def __init__(self, elements=None):
        """Initialize this binary tree with the given data."""
        self.tree = BinarySearchTree()
        if elements is not None:
            for element in elements:
                self.add(element)


    @property
    def size(self):
        """ Makes size an attribute """
        return self.tree.size


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





class HashSet(AbstractSet):
    def __init__(self, elements=None):
        """Initialize this hash table with the given data."""
        self.table = HashTable()
        if elements is not None:
            for element in elements:
                self.add(element)


    @property
    def size(self):
        """ Makes size an attribute """
        return self.tree.size


    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'Set({!r})'.format(self.table)


    def contains(self, item):
        return self.table.contains(item)


    def add(self, item):
        if not self.contains(item):
            self.table.set(item)


    def remove(self, item):
        self.table.delete(item)


    def items(self):
        return self.table.items()
