import numpy as np
import random
from minimum_cut import Graph
from queue import Queue

def shortest_path(graph, start_vertex, end_vertex):
    marked_vertecies = np.zeros(len(graph.vertices()))
    distances = np.zeros(len(graph.vertices()))
    marked_vertecies[start_vertex - 1] = 1
    queue = Queue()
    queue.push(start_vertex)
    while not queue.is_empty():
        removed_vertex = queue.pop()
        for edge in graph.graph_dict[str(removed_vertex)]:
            if marked_vertecies[edge - 1] != 1:
                marked_vertecies[edge - 1] = 1
                distances[edge - 1] += distances[removed_vertex - 1] + 1
                queue.push(edge)
    return int(distances[end_vertex - 1] - distances[start_vertex - 1])

example = {'1': [2, 3],
           '2': [1, 4],
           '3': [1, 4, 5],
           '4': [1, 3, 5, 6],
           '5': [2, 3, 5, 6],
           '6': [4, 5]}
example = Graph(example)

print(shortest_path(example, 1, 3))