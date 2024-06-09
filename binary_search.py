## taken from grokking algorithms book

def binary_search(list,item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid + 1
    return None

my_list = [1,3,5,7,9]

print(binary_search(my_list,3)) # 1
print(binary_search(my_list,-1)) # None


# Time complexity of binary search is O(log n), meaning time to complete algo increases logarithmically with the size of the input.

# Exercise 1
# 1.1 Suppose you have a sorted list of 128 names, and you're searching through it using binary search. What's the maximum number of steps it would take?
# log2(128) = 7

# 1.2 Suppose you double the size of the list. What's the maximum number of steps now?
# log2(256) = 8

# 1.3 You have a name, and you want to find the person's phone number in the phone book?
# O(log n) binary search

# 1.4 You have a phone number, and you want to find the person's name in the phone book. (Hint: You'll have to search through the whole book!)
# O(n) linear search

# 1.5 You want to read every person in the phone book?
# O(n) linear search

# 1.6 You want to read the numbers of just the As. 
# O(m + log n) where m is the number of As and n is the number of entries in the phone book.

# Recap Binary Search is a lot faster than simgple search
# O(log n) is faster than O(n), but it gets a lot faster once the list of items you're searching through grows. 
# Algo speed isn't measured in seconds, but in growth of the number of operations.
# Algo times are written in Big O notation.