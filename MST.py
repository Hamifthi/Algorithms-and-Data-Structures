from heap import Heap
from graph import Sub_Graph
from union_find import Union_Find
import numpy as np
import random
import sys

def prims_minimum_spanning_tree(graph: Sub_Graph):
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

        temp = np.array(list_of_vertices_key_values)
        min_vertex = temp[np.where(temp[:, 1] == str(minimum))[0][0]][0]

        list_of_mst_vertices.append(min_vertex)
        index = np.where(temp[:, 0] == min_vertex)[0][0]
        list_of_vertices_key_values.pop(index)

        for vertex, value in graph.graph_dict[min_vertex]:
            vertex = str(vertex)
            try:
                vertices = np.array(list_of_vertices_key_values)[:, 0]
            except IndexError:
                pass

            if vertex in vertices:
                index = np.where(vertices == vertex)[0][0]
                if value < list_of_vertices_key_values[index][1]:
                    heap.pop()
                    heap.insert(value)
                    list_of_vertices_key_values[index][1] = value

    return list_of_mst_vertices

def kruskals_minimum_spanning_tree(graph: Sub_Graph):
    list_of_mst_pairs = []
    list_of_sorted_distances = sorted(graph.distances)
    int_graph_vertices = [int(vertex) for vertex in graph.vertices]
    union_find_graph = Union_Find(int_graph_vertices)

    while len(list_of_sorted_distances) != 0:
        distance = list_of_sorted_distances[0]
        list_of_sorted_distances.pop(0)

        for pair in graph.pair_vertices.get(distance):
            vertex1, vertex2 = pair
            parent1, parent2 = union_find_graph.find_parent(vertex1), union_find_graph.find_parent(vertex2)

            if parent1 != parent2:
                union_find_graph.union(vertex1, vertex2)
                list_of_mst_pairs.append([vertex1, vertex2, distance])

    return list_of_mst_pairs

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
    # print(prims_minimum_spanning_tree(example))
    print(kruskals_minimum_spanning_tree(example))