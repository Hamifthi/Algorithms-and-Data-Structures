import random
import numpy as np
from graph import Graph
from queue import Queue
from BFS import breadth_first_search

def connected_components(graph):
    started_vertex = int(random.choice(graph.vertices()))
    stack_of_vertices = []
    stack_of_vertices.append(breadth_first_search(graph, started_vertex))
    for vertex in graph.vertices():
        list_of_traversed_vertices = [item for sublist in stack_of_vertices for item in sublist]
        if int(vertex) not in list_of_traversed_vertices:
            stack_of_vertices.append(breadth_first_search(graph, int(vertex)))
    return stack_of_vertices

if __name__=='__main__':
    example = {'1': [3, 5],
            '2': [4],
            '3': [1, 5],
            '4': [2],
            '5': [1, 3, 7, 9],
            '6': [8, 10],
            '7': [5],
            '8': [6, 10],
            '9': [5],
            '10':[6, 8]}
    example = Graph(example)

    print(connected_components(example))