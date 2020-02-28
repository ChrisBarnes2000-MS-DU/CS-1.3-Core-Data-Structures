from my_set import TreeSet
import unittest


class TreeSetTest(unittest.TestCase):

    def test_init(self):
        my_set = TreeSet()
        assert my_set.is_empty() is True
        assert my_set.items() == []
        assert my_set.contains(5) is False
        assert my_set.contains("hello") is False

    def test_add(self):
        my_set = TreeSet()
        assert my_set.is_empty() is True
        assert my_set.items() == []
        my_set.add(5)
        assert my_set.contains(5) is True
        assert my_set.contains(8) is False
        assert my_set.items() == [5]
        my_set.add(8)
        assert my_set.contains(8) is True
        assert my_set.items() == [5, 8]

if __name__ == '__main__':
    unittest.main()
