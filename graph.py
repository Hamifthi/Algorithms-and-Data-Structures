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
    def __init__(self, graph_dict):
        super().__init__(graph_dict, True)
        self.distances = []
        self.pair_vertices = {}
        self._make_lists()

    def add_edge(self, vertex1, vertex2, distance):
        self.graph_dict[str(vertex1)].append([vertex2, distance])

    def _make_lists(self):
        for key, value in self.graph_dict.items():
            for pair in value:
                self.distances.append(pair[1])
                self.pair_vertices[pair[1]] = [int(key), pair[0]]



if __name__=='__main__':
    # graph
    example1 = {'1': [2, 4],
           '2': [1, 3, 4],
           '3': [2, 4],
           '4': [1, 3, 2]}
    example1 = Graph(example1)
    print(example1.present_graph())
    example1.add_vertex([5])
    print(example1.present_graph())
    example1.add_edge(5, 2)
    example1.add_edge(5, 6)
    print(example1.present_graph())
    print(example1.vertices)
    print(example1.edges)
    # subgraph
    example2 = {'1': [[2, 3], [3, 6]],
            '2': [[4, 2]],
            '3': [[2, 1]],
            '4': [[1, 5], [3, 4]]
            }
    example2 = Sub_Graph(example2)
    print(example2.distances)
    print(example2.pair_vertices)