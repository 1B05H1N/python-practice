# breadth-first search
# chapter 6 - Graphs 
# Grokking Algorithms

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

from collections import deque

def person_is_seller(name):
    return name[-1] == 'm'  # Check if a person's name ends with 'm', indicating they are a mango seller

def search(graph, start):
    search_queue = deque()  # Create a new queue
    search_queue += graph[start]  # Add all of your neighbors to the search queue
    searched = []  # This list is how you keep track of which people you've searched before.
    
    while search_queue:
        person = search_queue.popleft()  # Take the first person off the queue
        if person not in searched:  # Only search this person if you haven't already searched them
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True  # Return from the search function, indicating a mango seller was found
            search_queue += graph[person]  # If not, add all of their neighbors to the search queue
            searched.append(person)
    return False  # Return from the search function, indicating no mango seller was found after complete search

# Example graph
graph = {
    "you": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": []
}

# Call the search function with the graph and start node
search(graph, "you")  # Start the search from 'you'

# recap
# Breadth-first search is a way to find the shortest path between two nodes in a graph.
# if you have a problem like "find the shortest X," try modeling your problem as a graph, and use breadth-first search to solve.
# A direxted graph has arrows, and the relationship follows the direction of the arrow.
# An undirected graph has no arrows, and the relationship goes both ways.
# Queues are FIFO (First In, First Out)
# Stacks are LIFO (Last In, First Out)
# You need to check people in the order they were added to the search list, so the search list needs to be a queue.
# The search list should keep track of people you've searched before to avoid infinite loops.
# Once you check someone, make sure you don't check them again. Otherwise, you might end up in an infinite loop.