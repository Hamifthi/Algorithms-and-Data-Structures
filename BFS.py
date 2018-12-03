import numpy as np
import random
from minimum_cut import Graph
from queue import Queue

def breadth_first_search(graph, started_vertex = None):
    marked_vertecies = np.zeros(len(graph.vertices()))
    if started_vertex == None:
        started_vertex = int(random.choice(graph.vertices()))
    traversed_vertecies = []
    marked_vertecies[started_vertex - 1] = 1
    queue = Queue()
    queue.push(started_vertex)
    traversed_vertecies.append(started_vertex)
    while not queue.is_empty():
        removed_vertex = queue.pop()
        for edge in graph.graph_dict[str(removed_vertex)]:
            if marked_vertecies[edge - 1] != 1:
                marked_vertecies[edge - 1] = 1
                traversed_vertecies.append(edge)
                queue.push(edge)
    return traversed_vertecies

if __name__=='__main__':
    example = {'1': [2, 4, 6],
            '2': [1, 3],
            '3': [2, 4, 5],
            '4': [1, 3, 5, 6],
            '5': [3, 4, 6],
            '6': [1, 4, 5]}
    example = Graph(example)

    print(breadth_first_search(example))