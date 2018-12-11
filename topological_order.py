import numpy as np
import random
from graph import Graph
from queue import Queue

def topological_order(graph):

    def recursive_topological_sort(vertex, marked_vertecies, queue):
        marked_vertecies[vertex - 1] = 1

        for edge in graph.graph_dict[str(vertex)]:
            if edge == None: break
            if marked_vertecies[edge - 1] == 0:
                recursive_topological_sort(edge, marked_vertecies, queue)
        
        queue.push(vertex)

    marked_vertecies = np.zeros(len(graph.vertices()))
    queue = Queue()

    for vertex in graph.vertices():
        vertex = int(vertex)
        if marked_vertecies[vertex - 1] == 0:
            recursive_topological_sort(vertex, marked_vertecies, queue)
    
    return queue.queue

if __name__=='__main__':
    example = {'1': [2, 3],
            '2': [],
            '3': [6],
            '4': [1, 3, 5],
            '5': [],
            '6': [],
            '7': [5, 6, 8, 9],
            '8': [5],
            '9': [8],
            '10': [9]}

    example2 = {'0': [],
            '1': [],
            '2': [3],
            '3': [1],
            '4': [0, 1],
            '5': [0, 2],
            }

    # example = Graph(example)
    # print(topological_order(example))
    example2 = Graph(example2)
    print(topological_order(example2))