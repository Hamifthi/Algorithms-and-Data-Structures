import numpy as np

def optimal_binary_search_trees(keys, frequencies):
    optimal_costs = np.zeros(shape = [len(keys), len(keys)])
    for i in range(len(keys)):
        optimal_costs[i, i] = frequencies[i]
    for l in range(2, len(keys) + 1):
        for i in range(len(keys)):
            j = i + l - 1
            costs = []
            frequency = sum(frequencies[i: j + 1])
            for r in range(i, j + 1):
                try:
                    costs.append(frequency + optimal_costs[i, r - 1] + optimal_costs[r + 1, j])
                except IndexError:
                    pass
            print(costs)
            try:
                optimal_costs[i, j] = np.min(costs)
                print(optimal_costs[i, j])
            except ValueError:
                pass
            except IndexError:
                pass
    return optimal_costs

if __name__ == '__main__':
    keys = [10, 20, 30]
    frequencies = [34, 8, 50]
    print(optimal_binary_search_trees(keys = keys, frequencies = frequencies))