# To find the maximum longest path in a Directed Acyclic Graph
# Import default dictionary container for dictionaries
from collections import defaultdict


class Graph:
    # Initialise attributes in a class inside the constructore method
    def __init__(self, vertices):
        # Initialise default dictionary for creating a graph using adjacency list
        self.graph = defaultdict(list)
        # Initialise vertices of the graph
        self.vertices = vertices

    # Add Edge method to add each item in the adjacancy list one by one
    # u = c1
    # v = c2
    # z = weights
    def addEdge(self, u, v, z):
        self.graph[u].append((v, z))

        """
        Function to find the topological sort of an adjacency list
        using recursive approach.

        ---------
        Parameters
        ---------
        Graph variable with graph class instance

        ---------
        Returns
        ---------
        A stack of c1, sorted

        ---------
        Time Complexity
        ---------
        O(V+E) as he adjacency list dominates the memory usage.

        ---------
        Test Cases
        ---------
            (0, 1, -21),
            (2, 1, -43),
            (3, 1, -18),
            (3, 0, -44),
            (2, 0, -23)
        => [3, 2, 0, 1]

        """

    def recursiveTopo(self, i, visited, stack):
        # mark the current node as True
        visited[i] = True

        for node, weight in self.graph[i]:
            if visited[node] == False:
                self.recursiveTopo(node, visited, stack)
        # Push the vertex value to the list
        stack.append(i)
        print(stack)

    def tSort(self, s):
        # Initially mark all vertices as not visited
        V = self.vertices
        visited = [False] * V
        # Initialise stack as an empty list for DFS
        stack = []
        for i in range(V):
            if visited[i] == False:
                self.recursiveTopo(s, visited, stack)
        return stack

    """
    Function to find the find the distance of a single source to all other nodes with -G transformation,
    by iterating nodes u of the graph in topological order: d[v]=min(d[v], d[u] + w(u,v))

    ---------
    Parameters
    ---------
    starting vertex

    ---------
    Returns
    ---------
    A list of distances

    ---------
    Time Complexity
    ---------
    O(V+E) lineat time

    """

    def longestPath(self, s):
        stack = self.tSort(s)
        # Initialize distances to all vertices as infinite and
        # distance to source as 0
        distanceNodes = [float(1)] * (self.vertices)
        distanceNodes[s] = 0

        # Process vertices in topological order
        while stack:

            # Get the next vertex from topological order
            last = stack.pop()

            # Update distanceNodesances of all adjacent vertices
            # d[v]=min(d[v], d[u] + w(u,v))
            for node, weight in self.graph[last]:
                # print(node)
                if distanceNodes[node] > distanceNodes[last] + weight:
                    distanceNodes[node] = distanceNodes[last] + weight

        for i in range(len(distanceNodes)):
            distanceNodes[i] = abs(distanceNodes[i])
        print(distanceNodes)
        return distanceNodes


testC = [('alpine_ridge', 7), ('rocky_canteen', 5),
         ('sunrise_ridge', 10), ('east_bluff', 10)]

testC = tuple(testC)
testList = [('rocky_canteen', 'alpine_ridge', 21), ('sunrise_ridge', 'rocky_canteen', 43), ('east_bluff',
                                                                                            'rocky_canteen', 18), ('east_bluff', 'alpine_ridge', 44), ('sunrise_ridge', 'alpine_ridge', 23)]

testList = tuple(testList)

vertices = list()

for i in range(len(testList)):
    vertices.append(testList[i][0])
    vertices.append(testList[i][1])
graph_length = len(list(set(vertices)))

# Initialising the graph with number of vertices
g = Graph(graph_length)

edges = defaultdict(list)
visited_list = defaultdict(list)

# for i in range(len(testList)):
#     g.addEdge(testList[i][0],testList[i][1], testList[i][2] )
#     edges[testList[i][0]].append(testList[i][1])
#     visited_list[testList[i][0]] = False

unique_vertices = list(set(vertices))
unique_dict = defaultdict(list)
for i in range(len(unique_vertices)):
    unique_dict[unique_vertices[i]].append(i)

# Adding Heights to a new tuple
# newCList = list()
newCDict = defaultdict(list)
for i in range(len(testC)):
    for key in unique_dict:
        if testC[i][0] == key:
            x = unique_dict[key][0]
    newCDict[x].append(testC[i][1])

# Creating a new tuple for Awesomness
new_dict = defaultdict(list)
newList = list()
for i in range(len(testList)):
    for key in unique_dict:
        if testList[i][0] == key:
            x = unique_dict[key][0]
        if testList[i][1] == key:
            y = unique_dict[key][0]
    new_dict[x].append(y)
    for key in newCDict:
        if x == key:
            x_val = newCDict[x][0]
        if y == key:
            y_val = newCDict[y][0]
    if x_val > y_val:
        k = (x, y, -testList[i][2])
    if y_val > x_val:
        k = (y, x, -testList[i][2])
    newList.append(k)
newTuple = tuple(newList)

for i in range(len(newTuple)):
    g.addEdge(newTuple[i][0], newTuple[i][1], newTuple[i][2])

finalArray = []
for i in range(0, graph_length):
    x = g.longestPath(i)
    finalArray.append(max(x))
print('Maximum Awesomeness is:', max(finalArray))
