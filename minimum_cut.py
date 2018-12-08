import numpy as np
import random
from graph import Graph

def minimum_cut(graph):
    graph_info = graph.graph_dict
    # put vertices in a seperate value to have how many numbers of it i have and also can delete from it
    vertices = list(graph.graph_dict.keys())
    while len(vertices) > 2:
        # choose an edge for merge
        edges = [edge for edges in graph_info.values() for edge in edges]
        edges = list(set(edges))
        edge = random.choice(edges)
        print(edge)

        # choose which vertex of selected edge i should merge
        vertex = random.choice([keys for keys, values in graph_info.items() for value in values if value == edge])
        print(vertex)
        vertices.remove(vertex)

        # delete connection or edges of merged vertex from connected vertices
        for key in graph_info.keys():
            try:
                sth = np.array(graph_info[str(key)])
                del graph_info[str(key)][np.where(sth == int(vertex))[0][0]]
            except IndexError:
                pass

        # transfer edges from merged vertex to new paired vertex
        for value in graph_info[vertex]:
            graph_info[str(edge)].append(value)
            graph_info[str(edge)] = list(set(graph_info[str(edge)]))
        del graph_info[vertex]

        # delete self loop
        for key, values in graph_info.items():
            values_copy = np.array(values)
            try:
                del graph_info[str(key)][np.where(values_copy == int(key))[0][0]]
            except IndexError:
                pass

        # print(len(self.__vertices))
        print(graph_info)

    min_edge = 0
    for value in graph_info.values():
        min_edge += len(value)
    return min_edge


if __name__=='__main__':
    example = {'1': [2, 4],
           '2': [1, 3, 4],
           '3': [2, 4],
           '4': [1, 3, 2]}

    example = Graph(example)
    print(minimum_cut(example))