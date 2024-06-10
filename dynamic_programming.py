# Chapter 9 - Dynamic Programming
# Grokking Algorithms

# Dynamic programming is a method for solving a complex problem by breaking it down into a collection of simpler subproblems, solving each of those subproblems just once, and storing their solutions.

# Dynamic programming only works when a problem has two key properties:
# 1. Overlapping subproblems
# 2. Optimal substructure

# Exercise 
# 9.2 

def knapsack(items, capacity):
    # Items: (weight, value)
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)] # DP table (n+1) x (capacity+1) initialized with 0
    
    # Fill the DP table
    for i in range(1, n + 1): # Start from the first item
        for w in range(1, capacity + 1): # Start from the first weight
            weight, value = items[i-1] # Current item
            if weight <= w: # If the current item can be included
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + value) # Choose the maximum value
            else:
                dp[i][w] = dp[i-1][w] # Exclude the current item

    # Find out which items to include
    result = []
    w = capacity
    for i in range(n, 0, -1): # Start from the last item
        if dp[i][w] != dp[i-1][w]: # If the value is different, include the item
            result.append(items[i-1])
            w -= items[i-1][0]

    return result[::-1], dp[n][capacity]

# Items (weight, value)
items = [(3, 10), (1, 3), (2, 9), (2, 5), (1, 6)]
capacity = 6

selected_items, max_value = knapsack(items, capacity)
print("Selected Items (weight, value):", selected_items)
print("Maximum Value:", max_value)

# Dynamic programming is useful when you're trying to optimize something given a constraint.
# You can use dynamic programming when the problem can be broken into discrete subproblems, and they don't depend on each other.

# Tips:
# Every dynamic programming solution involves a grid.
# The values in the cells are usually what you're trying to optimize.
# Each cell is a subproblem, so think about how you can divide your problem into subproblems.

# Feynman Algorithm:
# Write down the problem.
# Think really hard.
# Write down the solution.

# Levenshtein Distance measures the difference between two strings.

# Exercise
# 9.3 Draw and fill in the grid to calculate the logest common substring between blues and clues.

# 		C	L	U	E	S
#   0	0	0	0	0	0
# B	0	0	0	0	0	0
# L	0	0	1	0	0	0
# U	0	0	0	2	0	0
# E	0	0	0	0	3	0

# Recap
# Dynamic programming is useful when you're trying to optimize something given a constraint.
# You can use dynamic programming when the problem can be broken into discrete subproblems.
# Every dynamic programming solution involves a grid.
# The values in the cells are usually what you're trying to optimize.
# Each cell is a subproblem, so think about how you can divide your problem into subproblems.
# There's no single formula for calculating a dynamic programming solution.