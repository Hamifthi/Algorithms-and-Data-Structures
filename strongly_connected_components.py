import numpy as np
from graph import Graph
from stack import Stack

def strongly_connected_component(graph):

    def compute_reversed_graph(graph = graph):
        reversed_graph = {}
        reversed_graph = Graph(reversed_graph)

        for vertex in graph.vertices():
            reversed_graph.add_vertex(vertex)

        for vertex in graph.vertices():
            for edge in graph.graph_dict[str(vertex)]:
                reversed_graph.add_edge(edge, int(vertex))

        return reversed_graph

    def first_dfs(reversed_graph = compute_reversed_graph()):
        graph = reversed_graph
        stack = Stack()
        marked_vertecies = np.zeros(len(graph.vertices()))
        t = 1
        f_times = np.zeros(len(graph.vertices()))

        def recursive_depth_first_search(vertex, marked_vertecies, stack):
            nonlocal t
            if marked_vertecies[vertex - 1] == 0:
                marked_vertecies[vertex - 1] = 1
                stack.push(vertex)
            
                print(stack.stack)
                for edge in graph.graph_dict[str(vertex)]:
                    if edge == None: break
                    if marked_vertecies[edge - 1] == 0:
                        recursive_depth_first_search(edge, marked_vertecies, stack)
            else:
                try:
                    vertex = stack.pop()
                    f_times[vertex - 1] = t
                    t += 1
                except IndexError:
                    pass
        
        vertex = reversed_graph.vertices()[-1]
        recursive_depth_first_search(int(vertex), marked_vertecies, stack)

        for vertex in graph.vertices():
            vertex = int(vertex)
            if marked_vertecies[vertex - 1] == 0:
                recursive_depth_first_search(vertex, marked_vertecies, stack)

        return f_times

    return first_dfs

if __name__=='__main__':
    example = {'1': [4],
            '2': [8],
            '3': [6],
            '4': [7],
            '5': [2],
            '6': [9],
            '7': [1],
            '8': [5, 6],
            '9': [3, 7]
            }

    example = Graph(example)
    print(strongly_connected_component(example)())