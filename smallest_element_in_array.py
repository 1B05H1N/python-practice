# grokking algos - p.35

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

print(findSmallest([5, 3, 6, 2, 10])) # 3

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5, 3, 6, 2, 10])) # [2, 3, 5, 6, 10]

# Computer's memory is like a giant set of drawers
# When you want to store multiple elements, use an array or list
# With an array, all elements are stored right next to each other.
# With a list, elements are all over the place, and one element stores the address of the next one.
# Arrays allow fast reads
# Linked lists allow fast inserts and deletes
# All elements in an array should be the same type (all ints, all doubles....)