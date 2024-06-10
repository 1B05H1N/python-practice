# Grokking Algos Chapter 8

# Greedy Algorithms
# - A greedy algorithm is one that always takes the best immediate, or local, solution while finding an answer.
# - Greedy algorithms are easy to come up with and can be very efficient.
# - Greedy algorithms are not always the best solution.
# - Greedy algorithms are used on optimization problems.

# Example: The knapsack problem
# - You have a knapsack that can hold a total weight of up to 20 pounds.
# - You have the following items to choose from:
#   - a stereo that weighs 4 pounds and is worth $3000
#   - a laptop that weighs 3 pounds and is worth $2000
#   - a guitar that weighs 1 pound and is worth $1500
# - Which items do you put in the knapsack to maximize the value?
# - The greedy algorithm would choose the guitar, the laptop, and the stereo.

# Exercises

# 8.1 sort boxes, select based in priority, fix boxes efficiently, repeat until truck is full
# 8.2 7 days to see everything. Select the shortest path to see everything, use Dijkstra's algorithm

# example

states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()

best_station = None
states_covered = set()
for station, states_for_station in stations.items():
    covered = states_needed & states_for_station # intersection, an intersection is the set of elements that are common to two or more sets
    if len(covered) > len(states_covered): # if the station covers more states than the current best station
        best_station = station
        states_covered = covered

# a set union means "combine both sets, but remove any duplicates"
# a set intersection means "return only the items that are present in both sets"
# a set difference means "return the items that are in the first set, but not in the second set"

# fruits = set(["avocado", "tomato", "banana"])
# vegetables = set(["beetroot", "carrot", "tomato"])
# fruits | vegetables # this is a union, it returns a set containing all the items from both sets
# fruits & vegetables # this is an intersection, it returns a set containing only the items that are in both sets
# fruits - vegetables # this is a difference, it returns a set containing the items that are in the first set, but not in the second set

# final_stations.add(best_station)
# states_needed -= states_covered

while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    final_stations.add(best_station)
    states_needed -= states_covered

print(final_stations) # {'kone', 'ktwo', 'kthree', 'kfive'}

# The time complexity of this algorithm is O(n^2), where n is the number of stations. This is because the algorithm has to loop over all the stations n times. The time complexity of the set operations is O(1), so they don't affect the overall time complexity.

# Exercises , greedy or not? 
# Quicksort is a greedy algorithm. False, because it doesn't always take the best immediate solution.
# Breadth-first search is a greedy algorithm. False, becuase it doesn't always take the best immediate solution.
# Dijkstra's algorithm is a greedy algorithm. True, because it always takes the best immediate solution.

# NP-complete problems
# - NP-complete problems are problems for which no known algorithm can solve them quickly.
# - NP-complete problems are common in the real world.
# - If you ever come across an NP-complete problem, your best bet is to use an approximation algorithm.
# - Approximation algorithms don't always find the optimal solution, but they guarantee that they'll find a solution that is close to the best one.
# Traveling Salesperson Problem is an NP-complete problem. The problem is to find the shortest possible route that visits each city exactly once and returns to the origin city.

# NP giveaways
# Your algo runs quicky a handful of items but slows down with more items. NP-complete problems often run quickly with only a few items, but their run time grows quickly.
# "All combinations of X" usually points to an NP-complete problem. NP-complete problems often require trying all possible combinations of a set of items.
# Do you have to calcuculate "every possible version" of X? NP-complete problems often involve calculating every possible version of something.
# If your problem involves a sequence (such as a sequence of cities, as in the Traveling Salesperson Problem), it might be NP-complete.
# If your problem involves a set (such as a set of cities), it might be NP-complete.
# Can you restate the problem as the set cover problem or another NP-complete problem? If so, it might be NP-complete.

# Excercises

# 8.6 A postman needs to deliver to 20 homes. He needs to find the shortest route that goes to all 20 homes. Is this an NP-complete problem? Yes, because it involves finding the shortest route that goes to all 20 homes.
# 8.7 Finding the largest clique in a set of people. Is this an NP-complete problem? Yes, because it involves finding the largest clique in a set of people. A clique is a subset of people who are all friends with each other.
# 8.8 You're making a map of the USA, and you need to color adjacent states differently. How many colors do you need? This is the four-color map problem, which is NP-complete. You need four colors to color the map so that no two adjacent states have the same color.

# Recap
# Greedy algos optimize locally, hoping to end up with a global optimum. 
# NP-complete problems have no known fast solution. 
# If you have a NP-complete problem, your best bet is to use an approximation algorithm.
# Greedy algorithms are easy to write and fast to run, so they make good approximation algorithms.
