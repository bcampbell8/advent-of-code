#This is a shortest path problem. Probably best to construct a graph for this.
#Weighted graph... undirected

#How to store weights?
#How to store conections

#This problem doesn't actually *really* require a graph in that the input
#provided has every location linked to every other location. Therefore
#I just need to iterate through each set of locations and choose the smallest
#number for each set of paths.

import pdb

class GraphNode:
    def __init__(self, name):
        self.name = name

class GraphEdge:
    def __init__(self, weight, a, b):
        self.weight = weight
        self.endpoints = (a,b)
        self.endpoint_names = (a.name, b.name)

    def opposite(c):
        if(c in self.endpoints):
            if c == a:
                return b
            else:
                return a

        else:
            raise LookupError("Vertex not incident on edge")

class Graph:
    def __init__(self):
        self.size = 0
        self.vertices = []
        self.edges = []

    def add_vertex(self, name):
        node = GraphNode(name)
        self.vertices.append(node)
        self.size += 1

    def add_edge(self, node_a, node_b, weight):
        node1 = None
        node2 = None
        for node in self.vertices:
            if node_a == node.name:
                node1 = node
            elif node_b == node.name:
                node2 = node
        if node1 == None or node2 == None:
            raise LookupError("One / both nodes don't exist.")
        edge = GraphEdge(weight, node1, node2)
        self.edges.append(edge)

    def iterate_vertices(self):
        node_list = []
        for vertex in self.vertices:
            node_list.append(vertex.name)
        return node_list





#graph = Graph()
grid = {}
with open("input.md", 'r', encoding='utf-8') as f:
    for line in f:
        line = line.split(" ")
        line[4] = line[4].strip("\n")
        #print(line)
        if line[0] not in grid:
            grid[line[0]] = {}
        if line[2] not in grid:
            grid[line[2]] = {}
        grid[line[0]][line[2]] = line[4]
        grid[line[2]][line[0]] = line[4]
        '''
        vertex_list = graph.iterate_vertices()
        if line[0] not in vertex_list:
            graph.add_vertex(line[0])
        if line[2] not in vertex_list:
            graph.add_vertex(line[2])
        graph.add_edge(line[0], line[2], int(line[4]))
        '''
#breakpoint()

areas = []

evaluations = {}
for point in grid:
    areas.append(point)
distance = 0
areas2 = areas.copy()
#breakpoint()
for area in areas2:
    distance = 0
    areas = areas2.copy()
    current_location = area
    areas.remove(current_location)
    while len(areas) > 0:
        lowest = None
        for location in areas:
            if lowest == None or int(grid[current_location][location]) < int(grid[current_location][lowest]):
                lowest = location

        print(f"location chosen: {lowest}")
        distance += int(grid[current_location][lowest])
        current_location = lowest
        areas.remove(current_location)
    evaluations[area] = distance
    #breakpoint()

final_start = None
for area in evaluations:
    if final_start == None or evaluations[area] < evaluations[final_start]:
        final_start = area
print(f"With a starting point of {final_start} the smallest path is {evaluations[final_start]}")

#breakpoint()
'''
for node in graph.vertices:
    print(node.name)
for edge in graph.edges:
    print(edge.endpoint_names, edge.weight)
'''
