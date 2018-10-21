import os
import sys

class Edge(object):
    def __init__(self, start, end, cost):
        self.start = start
        self.end = end
        self.cost = cost

    def __str__(self):
        return '[{0}]--{1}-->[{2}]'.format(self.start, self.cost, self.end)


class Vertex(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

    def append(self, edge):
        self.edges.append(edge)

    def __contains__(self, edge):
        return edge in self.edges

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __str__(self):
        return str(self.value)
        

class Graph(object):
    def __init__(self, bidirectional=False):
        self.vertices = []
        self.bidirectional = bidirectional

    def add_vertex(self, vertex_name):
        self.vertices.append(Vertex(vertex_name))

    def add_edge(self, vertex_name_1, vertex_name_2, cost=1):
        v1 = next(vertex for vertex in self.vertices if vertex.value == vertex_name_1)
        v2 = next(vertex for vertex in self.vertices if vertex.value == vertex_name_2)
        edge = Edge(v1, v2, cost)
        v1.append(edge)
        if self.bidirectional:
            edge = Edge(v2, v1, cost)
            v2.append(edge)


    def get_edge(self, vertex_name_1, vertex_name_2):
        v1 = next(vertex for vertex in self.vertices if vertex.value == vertex_name_1)
        v2 = next(vertex for vertex in self.vertices if vertex.value == vertex_name_2)
        if v1 and v2:
            edge = next(edge for edge in v1.edges if edge.end == v2)
            return edge
        else:
            return None

    def get_neighbors(self, vertex_name):
        v1 = next(vertex for vertex in self.vertices if vertex.value == vertex_name)
        return v1.edges

    def get_vertex(self, vertex_name):
        return next(vertex for vertex in self.vertices if vertex.value == vertex_name)
    
        
        
