class Graph:
    def __init__(self, graph_dict, directed = False):
        if graph_dict == None:
            self.graph_dict = {}
        self.graph_dict = graph_dict
        self.type = directed

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
    
    def vertices(self):
        return list(self.graph_dict.keys())

    def edges(self):
        return list(self.graph_dict.values())

    def present_graph(self):
        return self.graph_dict


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