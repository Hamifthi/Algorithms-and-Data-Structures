from heap import Heap
from dijkstra_algorithm import Sub_Graph
import numpy as np
import random
import sys

def prims_minimum_spanning_tree(graph):
    list_of_mst_vertices = []
    list_of_vertices_key_values = []

    key_values = np.zeros(len(graph.vertices))
    for step in range(1, len(key_values)):
        key_values[step] = sys.maxsize

    list_of_vertices_key_values.append([graph.vertices[0], 0])
    for vertex in range(1, len(graph.vertices)):
        list_of_vertices_key_values.append([graph.vertices[vertex], sys.maxsize])

    heap = Heap(list(key_values))

    while heap.length > 0:
        minimum = int(heap.min())
        # print(minimum)

        temp = np.array(list_of_vertices_key_values)
        min_vertex = temp[np.where(temp[:, 1] == str(minimum))[0][0]][0]
        # print(min_vertex)

        list_of_mst_vertices.append(min_vertex)
        index = np.where(temp[:, 0] == min_vertex)[0][0]
        list_of_vertices_key_values.pop(index)
        # print(heap.heap)

        for vertex, value in graph.graph_dict[min_vertex]:
            vertex = str(vertex)
            # print(vertex, value)
            try:
                vertices = np.array(list_of_vertices_key_values)[:, 0]
            except IndexError:
                pass
            # print(vertices)

            if vertex in vertices:
                index = np.where(vertices == vertex)[0][0]
                if value < list_of_vertices_key_values[index][1]:
                    heap.pop()
                    heap.insert(value)
                    list_of_vertices_key_values[index][1] = value

        # print(heap.heap)
        # print(list_of_vertices_key_values)
    return list_of_mst_vertices



if __name__=='__main__':
    example = {'0': [[1, 4], [7, 8]],
            '1': [[0, 4], [7, 11], [2, 8]],
            '7': [[0, 8], [1, 11], [8, 7], [6, 1]],
            '2': [[1, 8], [8, 2], [5, 4], [3, 7]],
            '8': [[2, 2], [7, 7], [6, 6]],
            '6': [[7, 1], [8, 6], [5, 2]],
            '3': [[2, 7], [5, 14], [4, 9]],
            '5': [[6, 2], [2, 4], [3, 14], [4, 10]],
            '4': [[3, 9], [5, 10]]
            }
    example = Sub_Graph(example)
    print(prims_minimum_spanning_tree(example))