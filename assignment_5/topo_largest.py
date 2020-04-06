# To find the maximum longest path in a Directed Acyclic Graph
# Import default dictionary container for dictionaries
from collections import defaultdict
from collections import Counter

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

        output_stack = list()
        check_stack = list()
        for i in range(len(stack)):
            check_stack.append(stack[i])
        # lengthStack = len(stack)
        # ctrItem = -1
        for i in range(0, len(stack), 1):
            popItem = check_stack.pop()
            if popItem not in output_stack:
                output_stack.append(popItem)


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
        return distanceNodes, output_stack


testC = [('alpine_horizon', 94), ('sunrise_bluff', 104), ('sunrise_landing', 44), ('west_horizon', 90), ('alpine_ridge', 107), ('sunrise_peak', 113), ('alpine_cliff', 58), ('sparrow_canteen', 69), ('west_bluff', 88), ('sunrise_canteen', 102), ('sparrow_landing', 49), ('east_horizon', 120), ('rocky_summit', 103), ('bobcat_summit', 109), ('west_summit', 83), ('rocky_cliff', 105), ('west_lodge', 51), ('cozy_ridge', 53), ('sparrow_cliff', 89), ('sunrise_ridge', 111), ('alpine_point', 87), ('cozy_summit', 44), ('north_peak', 58), ('north_point', 100), ('eagle_point', 119), ('eagle_summit', 47), ('cozy_peak', 83), ('bobcat_landing', 119), ('north_landing', 104), ('bobcat_peak', 57), ('east_bluff', 69), ('north_ridge', 90), ('rocky_lodge', 68), ('sunrise_point', 67), ('eagle_bluff', 67), ('rocky_horizon', 70), ('cozy_point', 48), ('bobcat_horizon', 108), ('rocky_peak', 62), ('alpine_summit', 97)]
testC = tuple(testC)
testList = [('eagle_summit', 'rocky_summit', 285), ('rocky_lodge', 'bobcat_summit', 335), ('sunrise_point', 'cozy_summit', 198), ('rocky_lodge', 'north_point', 895), ('rocky_lodge', 'alpine_cliff', 919), ('west_horizon', 'alpine_horizon', 1051), ('eagle_point', 'sunrise_canteen', 1598), ('bobcat_horizon', 'rocky_cliff', 1167), ('west_summit', 'east_horizon', 649), ('eagle_summit', 'alpine_cliff', 995), ('cozy_ridge', 'sunrise_landing', 1657), ('eagle_summit', 'west_horizon', 473), ('bobcat_landing', 'sunrise_landing', 927), ('cozy_peak', 'sunrise_bluff', 1558), ('rocky_peak', 'north_landing', 1619), ('cozy_summit', 'cozy_ridge', 1682), ('alpine_summit', 'sunrise_canteen', 1921), ('eagle_bluff', 'north_point', 1787), ('bobcat_horizon', 'sunrise_point', 472), ('north_point', 'north_peak', 650), ('rocky_horizon', 'west_summit', 1680), ('north_point', 'west_summit', 819), ('rocky_lodge', 'alpine_ridge', 1149), ('bobcat_horizon', 'cozy_point', 793), ('sunrise_ridge', 'cozy_ridge', 50), ('bobcat_peak', 'alpine_horizon', 499), ('east_bluff', 'sparrow_cliff', 827), ('north_landing', 'eagle_summit', 639), ('rocky_horizon', 'east_bluff', 1906), ('north_peak', 'sunrise_landing', 1723), ('west_horizon', 'sunrise_bluff', 1493), ('cozy_summit', 'west_lodge', 935), ('cozy_peak', 'rocky_summit', 1259), ('sunrise_point', 'eagle_point', 1372), ('north_landing', 'west_horizon', 180), ('alpine_point', 'west_summit', 757), ('east_bluff', 'rocky_summit', 1018), ('cozy_ridge', 'west_summit', 1236), ('eagle_bluff', 'alpine_point', 1163), ('eagle_summit', 'eagle_point', 1286), ('eagle_point', 'east_horizon', 297), ('sunrise_point', 'bobcat_peak', 1062), ('rocky_horizon', 'rocky_summit', 33), ('alpine_ridge', 'sunrise_landing', 1452), ('north_landing', 'sparrow_landing', 482), ('eagle_summit', 'sunrise_bluff', 613), ('rocky_horizon', 'alpine_point', 208), ('north_landing', 'alpine_point', 1367), ('rocky_peak', 'alpine_horizon', 1944), ('eagle_summit', 'sunrise_landing', 242), ('cozy_summit', 'rocky_summit', 1591), ('sunrise_peak', 'sunrise_landing', 823), ('east_horizon', 'west_bluff', 330), ('cozy_point', 'north_ridge', 353), ('bobcat_landing', 'alpine_horizon', 121), ('east_bluff', 'east_horizon', 888), ('west_bluff', 'west_horizon', 1665), ('alpine_point', 'alpine_cliff', 1507), ('north_point', 'east_horizon', 1438), ('alpine_summit', 'sunrise_landing', 1139), ('bobcat_horizon', 'north_peak', 1409), ('sparrow_cliff', 'alpine_horizon', 402), ('cozy_peak', 'cozy_ridge', 71), ('alpine_point', 'alpine_ridge', 1130), ('north_ridge', 'cozy_summit', 1135), ('rocky_horizon', 'alpine_cliff', 1741), ('alpine_summit', 'sunrise_bluff', 384), ('eagle_bluff', 'rocky_summit', 455), ('north_ridge', 'cozy_peak', 1160), ('eagle_bluff', 'west_lodge', 1576), ('rocky_horizon', 'cozy_ridge', 1888), ('eagle_bluff', 'bobcat_landing', 686), ('alpine_cliff', 'sunrise_landing', 991), ('cozy_peak', 'north_point', 1400), ('eagle_bluff', 'sparrow_cliff', 1845), ('rocky_peak', 'bobcat_peak', 252), ('west_summit', 'alpine_horizon', 308), ('eagle_bluff', 'sunrise_ridge', 1115), ('bobcat_landing', 'sparrow_landing', 421), ('west_summit', 'sunrise_bluff', 91), ('alpine_summit', 'sparrow_cliff', 1783), ('north_ridge', 'sparrow_canteen', 324), ('rocky_horizon', 'sunrise_landing', 864), ('bobcat_landing', 'sparrow_cliff', 849), ('north_point', 'alpine_ridge', 933), ('cozy_ridge', 'alpine_cliff', 121), ('west_bluff', 'sunrise_peak', 49), ('north_landing', 'west_lodge', 367), ('west_lodge', 'alpine_horizon', 1026), ('cozy_peak', 'sparrow_landing', 1438), ('bobcat_peak', 'north_point', 892), ('north_landing', 'cozy_ridge', 631), ('east_bluff', 'sunrise_peak', 1140), ('rocky_horizon', 'cozy_summit', 601), ('rocky_horizon', 'east_horizon', 946), ('rocky_cliff', 'sparrow_landing', 497), ('eagle_bluff', 'sunrise_peak', 933), ('bobcat_horizon', 'sunrise_bluff', 262), ('cozy_summit', 'alpine_ridge', 1193), ('east_horizon', 'sparrow_landing', 1145), ('cozy_point', 'rocky_horizon', 333), ('rocky_horizon', 'alpine_horizon', 482), ('bobcat_peak', 'bobcat_landing', 291), ('eagle_bluff', 'sunrise_landing', 697), ('sparrow_canteen', 'sunrise_landing', 156), ('rocky_lodge', 'north_landing', 1898), ('eagle_summit', 'rocky_cliff', 928), ('rocky_lodge', 'west_summit', 508), ('bobcat_landing', 'west_summit', 170), ('bobcat_horizon', 'alpine_horizon', 1003), ('rocky_lodge', 'sunrise_canteen', 513), ('eagle_point', 'cozy_ridge', 32), ('rocky_horizon', 'sparrow_cliff', 1335), ('eagle_point', 'alpine_cliff', 1346), ('alpine_point', 'sunrise_bluff', 1643), ('west_bluff', 'sparrow_canteen', 1856), ('rocky_cliff', 'west_bluff', 14), ('bobcat_peak', 'alpine_ridge', 788), ('rocky_lodge', 'west_lodge', 731), ('east_bluff', 'eagle_point', 1638), ('rocky_horizon', 'west_lodge', 1447), ('rocky_lodge', 'eagle_point', 814), ('rocky_horizon', 'sunrise_peak', 1823), ('cozy_point', 'west_summit', 1556), ('cozy_ridge', 'bobcat_summit', 220), ('rocky_horizon', 'eagle_bluff', 231), ('north_ridge', 'north_landing', 653), ('sparrow_landing', 'sunrise_landing', 1747), ('bobcat_landing', 'alpine_cliff', 1310), ('sunrise_canteen', 'sunrise_peak', 524), ('alpine_summit', 'west_bluff', 1541), ('rocky_peak', 'rocky_summit', 63), ('north_peak', 'alpine_ridge', 564), ('rocky_peak', 'cozy_point', 848), ('bobcat_horizon', 'rocky_summit', 1515), ('bobcat_peak', 'rocky_summit', 768), ('eagle_bluff', 'east_bluff', 738), ('cozy_point', 'sparrow_cliff', 303), ('north_point', 'alpine_horizon', 1641), ('cozy_ridge', 'sunrise_canteen', 540), ('cozy_point', 'sunrise_canteen', 1891), ('alpine_summit', 'eagle_summit', 1227), ('sparrow_cliff', 'sunrise_peak', 1706), ('north_point', 'cozy_summit', 1410), ('bobcat_peak', 'north_landing', 1022), ('rocky_lodge', 'alpine_horizon', 1580), ('north_peak', 'sunrise_canteen', 581), ('cozy_peak', 'east_horizon', 1339), ('sunrise_point', 'sparrow_landing', 113), ('bobcat_peak', 'sparrow_landing', 1613), ('sparrow_landing', 'sparrow_canteen', 276), ('east_bluff', 'west_horizon', 1275), ('bobcat_peak', 'west_bluff', 157), ('bobcat_horizon', 'west_bluff', 294), ('sunrise_peak', 'alpine_ridge', 1219), ('alpine_summit', 'north_ridge', 137), ('bobcat_landing', 'sparrow_canteen', 712), ('north_ridge', 'sunrise_peak', 1209), ('eagle_point', 'sparrow_cliff', 166), ('eagle_bluff', 'sparrow_canteen', 1775), ('sparrow_canteen', 'alpine_horizon', 487), ('rocky_lodge', 'north_ridge', 704), ('sunrise_point', 'north_peak', 828), ('east_horizon', 'sunrise_canteen', 1849), ('eagle_point', 'rocky_summit', 1603), ('alpine_point', 'west_horizon', 1364), ('north_peak', 'sunrise_bluff', 1750), ('cozy_point', 'eagle_point', 94), ('sparrow_landing', 'sunrise_bluff', 779), ('sparrow_cliff', 'cozy_ridge', 1904), ('cozy_summit', 'sunrise_bluff', 1225), ('rocky_horizon', 'rocky_lodge', 1589), ('cozy_point', 'bobcat_peak', 326), ('east_bluff', 'north_landing', 829), ('cozy_summit', 'sunrise_canteen', 1657), ('bobcat_landing', 'rocky_summit', 1094), ('bobcat_horizon', 'eagle_point', 1247), ('alpine_summit', 'cozy_point', 1724), ('alpine_summit', 'alpine_horizon', 1081), ('sunrise_point', 'sparrow_cliff', 1843), ('bobcat_peak', 'west_lodge', 1050), ('eagle_point', 'sunrise_peak', 1036), ('cozy_point', 'bobcat_summit', 112), ('eagle_summit', 'sunrise_ridge', 142), ('cozy_summit', 'west_summit', 1948), ('rocky_cliff', 'sparrow_canteen', 798), ('bobcat_landing', 'rocky_cliff', 832), ('sparrow_cliff', 'west_summit', 1161), ('sunrise_ridge', 'sparrow_canteen', 1634), ('cozy_ridge', 'alpine_ridge', 1596), ('bobcat_summit', 'rocky_summit', 1890), ('bobcat_summit', 'east_horizon', 355), ('sunrise_point', 'alpine_point', 472), ('bobcat_summit', 'sunrise_peak', 435), ('rocky_lodge', 'sparrow_landing', 482), ('cozy_ridge', 'west_bluff', 1199), ('alpine_summit', 'sparrow_landing', 791), ('west_summit', 'sparrow_canteen', 573), ('eagle_bluff', 'west_bluff', 1152), ('west_lodge', 'west_bluff', 748)]
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
# printing for testing purpose
# print(unique_dict)
# print(newCDict)

for i in range(len(newTuple)):
    g.addEdge(newTuple[i][0], newTuple[i][1], newTuple[i][2])

finalArray = []
finalDict = defaultdict(list)
for i in range(0, graph_length):
    x, y = g.longestPath(i)
    finalDict[max(x)].append(y)
    finalArray.append(max(x))
# Loop over and get the final answer and most awesome route
finalAnswer = defaultdict(list)
for key in finalDict:
    if key == max(finalArray):
        finalAnswer[key].append(finalDict[key][0])
# Update the integers with their corresponding string value       
updatedList = list()
for i in range(len((finalAnswer[max(finalArray)][0]))):
    # print(finalAnswer[max(finalArray)][0][i])
    for key in unique_dict:
        if finalAnswer[max(finalArray)][0][i] == unique_dict[key][0]:
            finalAnswer[max(finalArray)][0][i] = key
# Checking for duplicate values
# print(Counter(finalAnswer[max(finalArray)][0]).keys())
# print(Counter(finalAnswer[max(finalArray)][0]).values())

print('Maximum Awesomeness is:', finalAnswer)
