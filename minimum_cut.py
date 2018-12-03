import numpy as np
import random

class Graph:
    def __init__(self, graph_dict):
        if graph_dict == None:
            self.graph_dict = {}
        self.graph_dict = graph_dict
        self.__vertices = []

    def add_vertex(self, list_of_vertices_name):
        for name in list_of_vertices_name:
            self.graph_dict[str(name)] = []
    
    def add_edge(self, vertex1, vertex2):
        for vertex in [vertex1, vertex2]:
            if str(vertex) not in self.graph_dict.keys():
                self.graph_dict[str(vertex)] = []
        self.graph_dict[str(vertex1)].append(vertex2)
        self.graph_dict[str(vertex2)].append(vertex1)
    
    def vertices(self):
        return list(self.graph_dict.keys())

    def edges(self):
        return list(self.graph_dict.values())

    def present_graph(self):
        return self.graph_dict

    def minimum_cut(self):
        graph_info = {**self.graph_dict}
        # put vertices in a seperate value to have how many numbers of it i have and also can delete from it
        self.__vertices = list(self.graph_dict.keys())
        while len(self.__vertices) > 2:
            # choose an edge for merge
            edges = [edge for edges in graph_info.values() for edge in edges]
            edges = list(set(edges))
            edge = random.choice(edges)
            print(edge)

            # choose which vertex of selected edge i should merge
            vertex = random.choice([keys for keys, values in graph_info.items() for value in values if value == edge])
            print(vertex)
            self.__vertices.remove(vertex)

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
    print(example.present_graph())
    example.add_vertex([5])
    print(example.present_graph())
    example.add_edge(5, 2)
    example.add_edge(5, 6)
    print(example.present_graph())
    print(example.vertices())
    print(example.edges())
    print(example.minimum_cut())