# chapter 4 divide and conquer grokking algos

def sum(arr):
    total = 0
    for x in arr:
        total += x # total = total + x
    return total

print(sum([1, 2, 3, 4, 5])) # 15

# 4.2 recursive sum
# recursive version of sum
def recursive_sum(arr):
    if arr == []: # base case
        return 0
    return arr[0] + recursive_sum(arr[1:]) # slice and return array and index 1 to end

print(recursive_sum([1, 2, 3, 4, 5])) # 15

# 4.3 find the max number in a list
def find_max(arr):
    if len(arr) == 1: # base case if array has only one element
        return arr[0]
    else:
        sub_max = find_max(arr[1:])
        return max(arr[0], sub_max)
    
array = [1, 2, 3, 4, 5]
print(find_max(array)) # 5

# 4.4 recursive binary search
def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        # if guess is too high then set high to mid - 1
        if guess > item:
            high = mid - 1
        # if guess is too low then set low to mid + 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3)) # 1
print(binary_search(my_list, -1)) # None

# quick sort

# quick sort with empty array
def quicksort(arr):
    if len(arr) < 2:
        return arr # base case, arrays with 0 or 1 element are already sorted
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot] # sub-array of all elements less than the pivot
        greater = [i for i in arr[1:] if i > pivot] 
        return quicksort(less) + [pivot] + quicksort(greater)
    
print(quicksort([10, 5, 2, 3])) # [2, 3, 5, 10]

# merge sort

# merge sort with empty array
def print_items(arr):
    for item in arr:
        print(item)

# sleep between printing items
from time import sleep
def print_items2(list):
    for item in list:
        sleep(1)
        print(item)

# How long would each of these take to run in Big O notation? 
# 4.5 Printing the value of each element in an array? O(n) -- n elements, n prints
# 4.6 Doubling the value of each element in an array? O(n) -- n elements, n doubles
# 4.7 Doubling the value of just the first element in an array? O(1) -- only one element
# 4.8 Creating a multiplication table with all the elements in the array? O(n^2) -- n elements, n * n elements 

# D&C works by breaking the problem into smaller chunks. If you're using D&C on a list, the base case is probably an empty array or an array with one element.
# D&C algorithms are often recursive.
# If you're impmlementing qs, choose a random element as the pivot. The avg runtime of qs is O(n log n).
# The constant in Big O notation can matter sometimes. That's why quicksort is faster than merge sort.
# The constant almost never matters for simple search algorithms. That's why we say binary search is O(log n), even though the constant is larger than that of linear search.