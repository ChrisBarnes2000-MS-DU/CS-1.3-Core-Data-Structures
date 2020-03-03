from my_set import TreeSet
import unittest


class TreeSetTest(unittest.TestCase):
    """size - property that tracks the number of elements in constant time
        contains(element) - return a boolean indicating whether element is in this set
        add(element) - add element to this set, if not present already
        remove(element) - remove element from this set, if present, or else raise KeyError"""
    def test_init(self):
        my_set = TreeSet()
        assert my_set.is_empty() is True
        assert my_set.items() == []
        assert my_set.size is 0
        assert my_set.contains(5) is False
        assert my_set.contains("hello") is False

    def test_add(self):
        my_set = TreeSet()
        assert my_set.is_empty() is True
        assert my_set.items() == []
        assert my_set.size is 0
        my_set.add(5)
        assert my_set.contains(5) is True
        assert my_set.contains(8) is False
        assert my_set.items() == [5]
        assert my_set.size is 1
        my_set.add(8)
        assert my_set.contains(8) is True
        assert my_set.items() == [5, 8]
        assert my_set.size is 2
        return my_set

    def test_remove(self):
        my_set = TreeSet([4, 2, 6, 1, 3, 5, 7])
        assert my_set.tree.root.data == 4
        assert my_set.tree.root.left.data == 2
        assert my_set.tree.root.right.data == 6
        assert my_set.tree.root.left.left.data == 1
        assert my_set.tree.root.left.right.data == 3
        assert my_set.tree.root.right.left.data == 5
        assert my_set.tree.root.right.right.data == 7

        assert my_set.contains(4) is True
        assert my_set.contains(5) is True
        assert my_set.contains(8) is False
        assert my_set.items() == [1,2,3,4,5,6,7]
        assert my_set.size is 7
        my_set.remove(4)

        assert my_set.tree.root.data == 5
        assert my_set.tree.root.left.data == 2
        assert my_set.tree.root.right.data == 6
        assert my_set.tree.root.left.left.data == 1
        assert my_set.tree.root.left.right.data == 3
        assert my_set.tree.root.right.right.data == 7
        assert my_set.tree.root.right.left == None

        assert my_set.contains(4) is False
        assert my_set.contains(5) is True
        assert my_set.contains(8) is False
        assert my_set.items() == [1, 2, 3, 5, 6, 7]
        assert my_set.size is 6
        my_set.remove(5)
        my_set.remove(6)

        assert my_set.tree.root.data == 7
        assert my_set.tree.root.left.data == 2
        assert my_set.tree.root.right == None
        assert my_set.tree.root.left.left.data == 1
        assert my_set.tree.root.left.right.data == 3

        assert my_set.contains(4) is False
        assert my_set.contains(5) is False
        assert my_set.contains(3) is True
        assert my_set.items() == [1, 2, 3, 7]
        assert my_set.size is 4

        my_set.remove(3)
        my_set.remove(2)
        my_set.remove(1)
        my_set.remove(7)

        assert my_set.is_empty() is True
        assert my_set.items() == []
        assert my_set.size is 0


class AbstractSetTest(unittest.TestCase):
    """union(other_set) - return a new set that is the union of this set and other_set
        intersection(other_set) - return a new set that is the intersection of this set and other_set
        difference(other_set) - return a new set that is the difference of this set and other_set
        is_subset(other_set) - return a boolean indicating whether other_set is a subset of this set"""
    def test_union(self):
        set_a = TreeSet([1,2,3,4,5])
        set_b = TreeSet([6,7,8,9,10])
        set_c = set_a.union(set_b)
        assert set_c.is_subset(set_a) is True
        assert set_c.is_subset(set_b) is True
        assert set_c.items() == [1,2,3,4,5,6,7,8,9,10]
        assert set_c.is_subset([5,10,30,80,20]) is False


    def test_intersection(self):
        set_a = TreeSet([1, 2, 3, 4, 5])
        set_b = TreeSet([2, 3, 4, 7, 8, 10])
        is_intersection = set_a.intersection(set_b)
        assert is_intersection.items() == [2, 3, 4]
        assert is_intersection.items() != [7, 8, 10]


    def test_difference(self):
        set_a = TreeSet([1, 2, 3, 4, 5])
        set_b = TreeSet([2, 3, 4, 7, 8, 10])
        is_difference = set_a.difference(set_b)
        assert is_difference.items() != [2, 3, 4]
        assert is_difference.items() == [1, 5, 7, 8, 10]


    def test_is_subset(self):
        set_a = TreeSet([1, 2, 3, 4, 5])
        is_subset = set_a.is_subset([2,3,4])
        assert is_subset is True
        
        set_b = TreeSet([2, 3, 4])
        is_subset = set_a.is_subset(set_b)
        assert is_subset is True
        
        set_c = TreeSet([5, 3, 4])
        is_subset = set_a.is_subset(set_c)
        assert is_subset is True

        set_d = TreeSet([6, 7, 8])
        is_subset = set_a.is_subset(set_d)
        assert is_subset is False



if __name__ == '__main__':
    unittest.main()
