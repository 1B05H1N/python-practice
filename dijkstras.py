# chapter 7 - Dijkstras Algorithm

# Dijkstra's algorithm is used to find the shortest path between two nodes in a graph.
# It can only be used on graphs with positive weighted edges.
# It's fast and efficient.

# to recap , dijkstra's has 4 steps:
# 1. Find the cheapest node. This is the node you can get to in the least amount of time.
# 2. Check whether there's a cheaper path to the neighbors of this node. If so, update their costs.
# 3. Repeat until you've done this for every node in the graph.
# 4. Calculate the final path.

# weights are used to calculate the cheapest path.
# weights are assigned to edges between nodes.
# weights can be time, distance, or any other unit of measurement.
# The algorithm uses these weights to find the shortest path.

# to calculate the shortest path in an unweighted graph, you can use breadth-first search.
# to calculate the shortest path in a weighted graph, you can use Dijkstra's algorithm.

# graphs can aslo have cycles.
# a cycle is a loop in the graph.
# cycles can cause problems for Dijkstra's algorithm.
# Dijkstra's algorithm works only when all the weights are positive.

# Dijkstra's algorithm is a greedy algorithm, that only works with directed acyclic graphs (DAGs).

# if you want to find the shortest path in a graph with cycles, you can use the Bellman-Ford algorithm.
# Bellman-Ford algorithm can handle graphs with negative weights.

# dijktra's algorigh example: 

# create a graph

graph = {}
graph["you"] =["alice", "bob", "claire"]

graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
print(graph["start"].keys())  # dict_keys(['a', 'b'])

# add the rest of the nodes and their neighbors

print(graph["start"].keys())  # dict_keys(['a', 'b'])
print(graph["start"]["a"])  # 6

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5 

graph["fin"] = {} # the finish node has no neighbors

# create the costs table

infinity = float("inf")

costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []

# find the lowest cost node

def find_lowest_code_node(costs):
    lowest_cost = float("inf") # initialize the lowest cost to infinity
    lowest_cost_node = None # initialize the lowest cost node to None
    for node in costs: # go through each node
        cost = costs[node] # get the cost of the current node
        if cost < lowest_cost and node not in processed: # if the cost is lower than the current lowest cost and the node has not been processed yet
            lowest_cost = cost # update the lowest cost to the cost of the current node
            lowest_cost_node = node # update the lowest cost node to the current node
    return lowest_cost_node

while node is not None: # this loop runs until all the nodes have been processed
    cost = costs[node] # get the cost of the current node
    neighbors = graph[node] # get the neighbors of the current node
    for n in neighbors.keys(): # go through all the neighbors of the current node
        new_cost = cost + neighbors[n] # calculate the new cost to the neighbor
        if costs[n] > new_cost: # if the new cost is lower than the current cost
            costs[n] = new_cost # update the cost for this node
            parents[n] = node # this node becomes the new parent for this neighbor
    processed.append(node) # mark the node as processed
    node = find_lowest_code_node(costs) # find the next node to process and loop

# recap
# breadth-first search can be used to find the shortest path in an unweighted graph.
# Dijkstra's algorithm can be used to find the shortest path in a weighted graph.
# Dijkstra's algorithm works only with positive weights.
# If you have negative weights, use the Bellman-Ford algorithm.