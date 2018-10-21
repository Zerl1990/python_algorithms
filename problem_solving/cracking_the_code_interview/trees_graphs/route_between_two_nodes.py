# Route Between Nodes: Given a directed graph, design and
# algorithm to find out wheter there is a route between two nodes
import os
import sys
from graph import Graph

def is_path_between_nodes(vertex_a, vertex_b):
    visited = [vertex_a]

    # Deep copy
    queue = [edge.end for edge in vertex_a.edges]

    while queue:
        visit = queue.pop(0)
        if visit == vertex_b:
            return True
        elif visit not in queue:
            visited.append(visit)
            queue.extend(edge.end for edge in visit.edges)
            
        else:
            continue
            

    return False
    

if __name__ == '__main__':
    graph = Graph(bidirectional=False)
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)

    graph.add_edge(1,2)
    graph.add_edge(4,1)
    graph.add_edge(5,2)
    graph.add_edge(3,2)

    print is_path_between_nodes(graph.get_vertex(4), graph.get_vertex(5))


    
