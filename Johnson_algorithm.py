from graph import Sub_Graph
from shortest_path import Bellman_Ford_algorithm
from dijkstra_algorithm import dijkstra

def johnson_algorithm(graph):
    # make another graph name g_prime and add a source vertex with path zero to all other vertex
    g_prime = dict(graph.graph_dict)
    g_prime['s'] = [[int(vertex), 0] for vertex in graph.vertices]
    g_prime = Sub_Graph(g_prime)

    # calculate shortest path to all other vertices using new added vertex (s) with bellman_ford algorithm
    vertices_weights = Bellman_Ford_algorithm(graph = g_prime, src = 's')

    # now we delete last element of distances to remove source vertex (s) also delete g_prime
    vertices_weights.pop('s')
    del g_prime

    # calculate new edge weights using vertices_weights
    for vertex, edges in graph.graph_dict.items():
        try:
            list_of_edge_weights = []
            for edge, weight in edges:
                new_weight = weight + vertices_weights.get(vertex) - vertices_weights.get(str(edge))
                list_of_edge_weights.append([edge, new_weight])
                graph.graph_dict[vertex] = list_of_edge_weights
        except ValueError:
            pass
    
    # now we calculate shortest_path with dijkstra_algorithm
    for vertex in graph.vertices:
        print(vertex)
        shortest_paths = dijkstra(graph, int(vertex))
        print(shortest_paths)

    

if __name__=='__main__':
    example = {'0': [[1, -5], [2, 2], [3, 3]],
            '1': [[2, 4]],
            '2': [[3, 1]],
            '3': [[]]
            }
    example = Sub_Graph(example)
    johnson_algorithm(example)