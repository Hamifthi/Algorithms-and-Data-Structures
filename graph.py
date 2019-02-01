import numpy as np

class Graph:
    def __init__(self, graph_dict, directed = False):
        if graph_dict == None:
            self.graph_dict = {}
        self.graph_dict = graph_dict
        self.type = directed
        self.vertices = list(self.graph_dict.keys())
        self.edges = list(self.graph_dict.values())

    def add_vertex(self, list_of_vertices_name):
        for name in list_of_vertices_name:
            self.graph_dict[str(name)] = []
    
    def add_edge(self, vertex1, vertex2):
        for vertex in [vertex1, vertex2]:
            if str(vertex) not in self.graph_dict.keys():
                self.graph_dict[str(vertex)] = []
        if self.type:
            self.graph_dict[str(vertex1)].append(vertex2)
            self.graph_dict[str(vertex2)].append(vertex1)
        else:
            self.graph_dict[str(vertex1)].append(vertex2)

    def present_graph(self):
        return self.graph_dict

class Sub_Graph(Graph):
    def __init__(self, graph_dict, want = False):
        super().__init__(graph_dict, True)
        if want:
            self.distances = []
            self._make_list_of_distances()
            self.pair_vertices = {int(key):[] for key in self.distances}
            self._make_list_of_pair_vertices()

    def add_edge(self, vertex1, vertex2, distance):
        self.graph_dict[str(vertex1)].append([vertex2, distance])

    def _make_list_of_distances(self):
        for value in self.graph_dict.values():
            for pair in value:
                self.distances.append(pair[1])
        self.distances = list(set(self.distances))

    def _make_list_of_pair_vertices(self):
        for key, value in self.graph_dict.items():
            for pair in value:
                if len(self.pair_vertices.get(pair[1])) == 0:
                    self.pair_vertices[pair[1]].append([int(key), pair[0]])
                else:
                    last_pair = np.array(self.pair_vertices.get(pair[1])).flatten()
                    vertex1, vertex2 = [int(key), pair[0]]
                    if vertex1 not in last_pair:
                        self.pair_vertices[pair[1]].append([int(key), pair[0]])
    


if __name__=='__main__':
    # graph
    # example1 = {'1': [2, 4],
    #        '2': [1, 3, 4],
    #        '3': [2, 4],
    #        '4': [1, 3, 2]}
    # example1 = Graph(example1)
    # print(example1.present_graph())
    # example1.add_vertex([5])
    # print(example1.present_graph())
    # example1.add_edge(5, 2)
    # example1.add_edge(5, 6)
    # print(example1.present_graph())
    # print(example1.vertices)
    # print(example1.edges)
    # subgraph
    example2 = {'0': [[1, 4], [7, 8]],
            '1': [[0, 4], [7, 11], [2, 8]],
            '7': [[0, 8], [1, 11], [8, 7], [6, 1]],
            '2': [[1, 8], [8, 2], [5, 4], [3, 7]],
            '8': [[2, 2], [7, 7], [6, 6]],
            '6': [[7, 1], [8, 6], [5, 2]],
            '3': [[2, 7], [5, 14], [4, 9]],
            '5': [[6, 2], [2, 4], [3, 14], [4, 10]],
            '4': [[3, 9], [5, 10]]
            }
    example2 = Sub_Graph(example2)
    print(example2.distances)
    print(example2.pair_vertices)