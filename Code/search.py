#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # Time Complexity!
    # Best: O(1) - First element
    # Average: O(n) - Have to loop through every element in the array
    # Worst: O(n) - Have to loop through every element in the array
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # Time Complexity!
    # Best: O(1) - First element
    # Average: O(n) - Have to loop through every element in the array
    # Worst: O(n) - Have to loop through every element in the array
    if item == array[index]:
        return index
    else:
        nxt = index + 1
        return linear_search_recursive(array, item, nxt)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(arr, item):
    # Time Complexity!
    # Best: O(1) - Middle element is the item
    # Average: O(log(n)) - Because we halve the working array every time
    # Worst: O(log(n)) - Even if it is the last possible iteration, it will still be log(n) time
    # Iterative Binary Search Function
    # It returns location of x in given array arr if present,
    # else returns -1
    l = 0
    h = len(arr) -1
    while l <= h:
        mid_pos = (l + h) // 2
        mid = arr[mid_pos]
        # print('low[{}] mid[{}] high[{}] target[{}] looking at[{}]'.format(l,mid_pos, r, item, mid))
        # Check if item is present at mid
        if mid == item:
            return mid_pos
        # If item is greater, ignore left half
        elif mid < item:
            l = mid_pos + 1
        # If item is smaller, ignore right half
        else:
            h = mid_pos - 1
        # If we reach here, then the element was not present
    return -1

def binary_search_recursive(array, item, left=None, right=None):
    # Time Complexity!
    # Best: O(1) - Middle element is the item
    # Average: O(log(n)) - Because we halve the working array every time
    # Worst: O(log(n)) - Even if it is the last possible iteration, it will still be log(n) time
    if left is None and right is None:
        left = 0
        right = len(array) - 1
    if left > right:
        return -1
    mid_pos = (right + left) // 2
    if array[mid_pos] == item:
        return mid_pos
    elif array[mid_pos] > item:
        return binary_search_recursive(array, item, left, mid_pos - 1)
    elif array[mid_pos] < item:
        return binary_search_recursive(array, item, mid_pos + 1, right)


if __name__ == "__main__":
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    
    # arr = [5,3,4,2,6,1]
    # x = 4
    arr = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
    # x = 'Julia'
    # x = 'Nabil'
    x = 'chris'

    # print('index: ', linear_search(arr, 2))
    result = binary_search(arr, x)

    if result != -1:
        print ("Element {} is present at index {}".format(x, result))
    else:
        print ("Element is not present in array")
