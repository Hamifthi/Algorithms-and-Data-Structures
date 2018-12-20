from graph import Graph
import numpy as np

class Sub_Graph(Graph):
    def __init__(self, graph_dict):
        super().__init__(graph_dict, True)

    def add_edge(self, vertex1, vertex2, distance):
        self.graph_dict[str(vertex1)].append([vertex2, distance])

def dijkstra(graph):
    processed_vertices = []
    unprocessed_vertices = []
    total_distances = np.zeros(len(graph.vertices()))
    for step in range(1, len(total_distances)):
        total_distances[step] = np.inf
    for vertex in graph.vertices():
        unprocessed_vertices.append(vertex)

    distances = [0]

    while len(unprocessed_vertices) != 0:
        value = np.min(distances)
        # print(value)
        vertex = np.where(total_distances == value)[0][0]
        # print(vertex)
        # print(graph.vertices()[vertex])
        for edge, distance in graph.graph_dict[str(graph.vertices()[vertex])]:
            if total_distances[edge - 1] > total_distances[vertex] + distance:
                total_distances[edge - 1] = total_distances[vertex] + distance
                distances = np.append(distances, total_distances[vertex] + distance)
        processed_vertices.append(graph.vertices()[vertex])
        try:
            unprocessed_vertices.remove(graph.vertices()[vertex])
        except ValueError:
            pass
        item = np.where(distances == value)[0][0]
        distances = np.delete(distances, item)
        # print(processed_vertices)
        # print(unprocessed_vertices)
        # print(total_distances)

    return total_distances

if __name__=='__main__':
    example = {'1': [[2, 3], [3, 6]],
            '2': [[4, 2]],
            '3': [[2, 1]],
            '4': [[1, 5], [3, 4]]
            }
    example = Graph(example)
    print(dijkstra(example))