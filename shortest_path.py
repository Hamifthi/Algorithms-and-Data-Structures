import numpy as np
import random
from graph import Graph
from graph import Sub_Graph
from queue import Queue

def shortest_path(graph, start_vertex, end_vertex):
    marked_vertices = np.zeros(len(graph.vertices))
    distances = np.zeros(len(graph.vertices))
    queue = Queue()

    marked_vertices[start_vertex - 1] = 1
    queue.push(start_vertex)

    while not queue.is_empty():
        removed_vertex = queue.pop()
        for edge in graph.graph_dict[str(removed_vertex)]:
            if marked_vertices[edge - 1] != 1:
                marked_vertices[edge - 1] = 1
                distances[edge - 1] += distances[removed_vertex - 1] + 1
                queue.push(edge)

    return int(distances[end_vertex - 1] - distances[start_vertex - 1])

def Bellman_Ford_algorithm(graph, src):
    # intialize all distances with infinity and source vertex to zero
    distances = {key:np.inf for key in graph.vertices}
    distances[str(src)] = 0
    # iterate through the graph and update the distances
    for i in range(len(graph.vertices) - 1):
        for u in graph.vertices:
            if len(graph.graph_dict[u][0]) != 0:
                for v, w in graph.graph_dict[u]:
                    if distances[u] != np.inf and distances[u] + w < distances[str(v)]:
                        distances[str(v)] = distances[u] + w

    for i in range(len(graph.vertices) - 1):
        for u in graph.vertices:
            if len(graph.graph_dict[u][0]) != 0:
                for v, w in graph.graph_dict[u]:
                    if distances[u] != np.inf and distances[u] + w < distances[str(v)]:
                        print('graph contain negative weight cycle')
                        return
    
    return distances
 
if __name__=='__main__':
    example1 = {'1': [2, 3],
            '2': [1, 4],
            '3': [1, 4, 5],
            '4': [1, 3, 5, 6],
            '5': [2, 3, 5, 6],
            '6': [4, 5]}

    example1 = Graph(example1)
    print(shortest_path(example1, 1, 3))
    example2 = {'1': [[2, -1], [3, 4]],
            '2': [[3, 3], [4, 2], [5, 2]],
            '3': [[]],
            '4': [[2, 1]],
            '5': [[4, -3]]
            }
    example2 = Sub_Graph(example2)
    print(Bellman_Ford_algorithm(example2, 1))