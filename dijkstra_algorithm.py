from graph import Sub_Graph
import numpy as np

def dijkstra(graph, src:int):
    unprocessed_vertices = []
    total_distances = np.zeros(len(graph.vertices))
    
    for step in range(len(total_distances)):
        total_distances[step] = np.inf
    for vertex in graph.vertices:
        unprocessed_vertices.append(vertex)

    total_distances[src] = 0
    distances = [0]

    while len(unprocessed_vertices) != 0:
        try:
            value = np.min(distances)
        except ValueError:
            return total_distances
        i = 0
        vertex = np.where(total_distances == value)[0][i]
        if str(vertex) not in unprocessed_vertices:
            while str(vertex) not in unprocessed_vertices:
                i += 1
                vertex = np.where(total_distances == value)[0][i]

        try:
            for edge, distance in graph.graph_dict[str(vertex)]:
                if total_distances[edge] > total_distances[vertex] + distance:
                    try:
                        index = np.where(distances == total_distances[edge])[0][0]
                        distances = np.delete(distances, index)
                    except IndexError:
                        pass
                    total_distances[edge] = total_distances[vertex] + distance
                    distances = np.append(distances, total_distances[vertex] + distance)
        except ValueError:
            pass

        unprocessed_vertices.remove(str(vertex))

        item = np.where(distances == value)[0][0]
        distances = np.delete(distances, item)

    return total_distances

if __name__=='__main__':
    example = {'0': [[1, 4], [7, 8]],
            '1': [[0, 4], [7, 11], [2, 8]],
            '7': [[0, 8], [1, 11], [8, 7], [6, 1]],
            '2': [[1, 8], [8, 2], [5, 4], [3, 7]],
            '8': [[2, 2], [7, 7], [6, 6]],
            '6': [[7, 1], [8, 6], [5, 2]],
            '3': [[2, 7], [5, 14], [4, 9]],
            '5': [[6, 2], [2, 4], [3, 14], [4, 10]],
            '4': [[3, 9], [5, 10]]
            }
    example = Sub_Graph(example)
    print(dijkstra(example, 4))