import numpy as np
import random
from graph import Graph

def depth_first_search(graph, vertex = None, first_time = False):
    if first_time:
        global marked_vertecies
        global traversed_vertecies
        marked_vertecies = np.zeros(len(graph.vertices()))
        traversed_vertecies = []

        if vertex == None:
            started_vertex = int(random.choice(graph.vertices()))
            while len(graph.graph_dict[str(started_vertex)]) == 0:
                started_vertex = int(random.choice(graph.vertices()))
            vertex = started_vertex

        marked_vertecies[vertex - 1] = 1
        traversed_vertecies.append(vertex)
        print(vertex)
    
    for edge in graph.graph_dict[str(vertex)]:
        if vertex not in traversed_vertecies:
            marked_vertecies[vertex - 1] = 1
            traversed_vertecies.append(vertex)

        if edge == None: break

        if marked_vertecies[edge - 1] != 1:
            marked_vertecies[edge - 1] = 1
            traversed_vertecies.append(edge)
            depth_first_search(graph, edge)
    
    return traversed_vertecies, marked_vertecies

def traverse_entire_graph(graph):
    traversed_vertecies, marked_vertecies = depth_first_search(graph, first_time = True)
    all_traversed_vetices = []
    all_traversed_vetices.append(traversed_vertecies)
    untraversed_vertices = np.where(marked_vertecies != 1)[0]
    for vertex in untraversed_vertices:
        all_traversed_vetices.append(depth_first_search(graph, vertex = vertex + 1, first_time = True)[0])

    return list(set([item for vertices in all_traversed_vetices for item in vertices]))


def depth_first_search_v2(graph, vertex = None):

    def recursive_depth_first_search(vertex, marked_vertecies):
        marked_vertecies[vertex - 1] = 1

        for edge in graph.graph_dict[str(vertex)]:
            if edge == None: break
            if marked_vertecies[edge - 1] == 0:
                recursive_depth_first_search(edge, marked_vertecies)

        traversed_vertecies.append(vertex)
    

    marked_vertecies = np.zeros(len(graph.vertices()))
    traversed_vertecies = []

    if vertex == None:
        started_vertex = int(random.choice(graph.vertices()))
        while len(graph.graph_dict[str(started_vertex)]) == 0:
            started_vertex = int(random.choice(graph.vertices()))
        vertex = started_vertex

    recursive_depth_first_search(vertex, marked_vertecies)

    for vertex in graph.vertices():
        vertex = int(vertex)
        if marked_vertecies[vertex - 1] == 0:
            recursive_depth_first_search(vertex, marked_vertecies)

    return traversed_vertecies, marked_vertecies






if __name__=='__main__':
    example = {'1': [2, 4],
            '2': [3],
            '3': [4, 5],
            '4': [],
            '5': []}

    example = Graph(example)
    print(depth_first_search_v2(example))