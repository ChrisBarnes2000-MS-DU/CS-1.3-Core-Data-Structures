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
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # Time Complexity!
    # Best: O(1) - Middle element is the item
    # Average: O(log(n)) - Because we halve the working array every time
    # Worst: O(log(n)) - Even if it is the last possible iteration, it will still be log(n) time
    first = 0
    last = len(array)-1
    target = False
    while(first <= last and not target):
        mid = (first + last)//2
        if array[mid] == item:
            target = True
        else:
            if item < array[mid]:
                last = mid - 1
            else:
                first = mid + 1
        return target


def binary_search_recursive(array, item, left=None, right=None):
    # Time Complexity!
    # Best: O(1) - Middle element is the item
    # Average: O(log(n)) - Because we halve the working array every time
    # Worst: O(log(n)) - Even if it is the last possible iteration, it will still be log(n) time
    pass

if __name__ == "__main__":
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    
    arr = [5,3,4,2,6,1]
    # print('index: ', linear_search(arr, 2))
    # print(binary_search([1, 2, 3, 5, 8], 6))
    # print(binary_search([1, 2, 3, 5, 8], 5))
    print(binary_search([1, 2, 3, 5, 6, 8, 9], 2))
    # print('found 2: ', binary_search(arr, 2))
