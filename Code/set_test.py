from my_set import TreeSet
import unittest


class TreeSetTest(unittest.TestCase):
    """
        size - property that tracks the number of elements in constant time
        contains(element) - return a boolean indicating whether element is in this set
        add(element) - add element to this set, if not present already
        remove(element) - remove element from this set, if present, or else raise KeyError
    """


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

    # def test_remove(self):
    #     my_set = self.test_add()
    #     assert my_set.contains(5) is True
    #     assert my_set.contains(8) is True
    #     assert my_set.items() == [5, 8]
    #     assert my_set.size is 2
    #     my_set.remove(8)
    #     assert my_set.contains(5) is True
    #     assert my_set.contains(8) is False
    #     assert my_set.items() == [5]
    #     assert my_set.size is 1
    #     my_set.remove(5)
    #     assert my_set.is_empty() is True
    #     assert my_set.items() == []
    #     assert my_set.size is 0




class AbstractSetTest(unittest.TestCase):
    """
    union(other_set) - return a new set that is the union of this set and other_set
    intersection(other_set) - return a new set that is the intersection of this set and other_set
    difference(other_set) - return a new set that is the difference of this set and other_set
    is_subset(other_set) - return a boolean indicating whether other_set is a subset of this set
    """
    # def test_union(self):
    #     set_a = TreeSet([1,2,3,4,5])
    #     set_b = TreeSet([6,7,8,9,10])

    #     set_c = set_a.union(set_b)
    #     print(set_a)
    #     print(set_b)

    # def test_intersection(self):
    #     set_a = TreeSet([1, 2, 3, 4, 5])
    #     set_b = [2, 3, 4]


    # def test_difference(self):
    #     pass


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



    # def test_function(self):
        # assert False == True
    #     pass
    


if __name__ == '__main__':
    unittest.main()
