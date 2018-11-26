class Graph:
    def __init__(self, graph_dict):
        if graph_dict == None:
            self.__graph_dict = {}
        self.__graph_dict = graph_dict

    def add_vertex(self, list_of_vertices_name):
        for name in list_of_vertices_name:
            self.__graph_dict[str(name)] = []
    
    def add_edge(self, vertex1, vertex2):
        for vertex in [vertex1, vertex2]:
            if str(vertex) not in self.__graph_dict.keys():
                self.__graph_dict[str(vertex)] = []
        self.__graph_dict[str(vertex1)].append(vertex2)
        self.__graph_dict[str(vertex2)].append(vertex1)
    
    def present_vertecies(self):
        return list(self.__graph_dict.keys())

    def present_edges(self):
        return list(self.__graph_dict.values())

    def present_graph(self):
        return self.__graph_dict

example = {'1': [2, 3],
           '2': [1, 4],
           '3': [2, 4],
           '4': [1, 3]}

example = Graph(example)
print(example.present_graph())
example.add_vertex([5])
print(example.present_graph())
example.add_edge(5, 2)
example.add_edge(5, 6)
print(example.present_graph())
print(example.present_vertecies())
print(example.present_edges())