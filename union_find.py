class Node:
    def __init__(self, value, parent = None):
        self.value = value
        self.parent = parent
        self.group = []

class Union_Find:
    def __init__(self, list_of_values):
        self.values = []
        for item in list_of_values:
            self.values.append(Node(value = item, parent = item))
        
    def add_node(self, value, parent):
        parent_value = self.find_parent(parent)
        if parent_value != None:
            node = Node(value, parent_value)
            self.values.append(node)
            parent_node = self.find_node(value = parent_value)
            parent_node.group.append(node)
        else:
            self.values.append(Node(value = value, parent = value))

    def find_parent(self, value):
        for node in self.values:
            if node.value == value: return node.parent
        return None

    def find_node(self, value):
        for node in self.values:
            if node.value == value: return node
        return None

    def union(self, value1, value2):
        node1, node2 = self.find_node(value = value1), self.find_node(value = value2)
        parent_value1, parent_value2 = self.find_parent(value = node1.value), self.find_parent(value = node2.value)
        parent_node1, parent_node2 = self.find_node(value = parent_value1), self.find_node(value = parent_value2)

        if len(parent_node1.group) >= len(parent_node2.group):
            for node in parent_node2.group:
                node.parent = node1.parent
                parent_node1.group.append(node)
            node2.parent = node1.parent
            parent_node1.group.append(node2)
        else:
            for node in node1.group:
                node.parent = node2.parent
                parent_node2.group.append(node)
            node1.parent = node2.parent
            parent_node2.group.append(node1)

if __name__=='__main__':
    sth = [1, 2, 3, 4]
    sth = Union_Find(sth)
    print(sth.values)
    sth.union(1, 2)
    sth.union(1, 3)
    print(sth.find_node(1).group[0].value)
    print(sth.find_node(1).group[1].parent)
    sth.add_node(5, 1)
    print(sth.find_node(1).group)