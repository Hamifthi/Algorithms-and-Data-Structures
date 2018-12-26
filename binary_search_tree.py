class Node:
    def __init__(self, value, parent = None, left_child = None, right_child = None):
        self.value = value
        self.parent = parent
        if left_child != None and not left_child.value <= self.value:
            raise ValueError
            print('left child must be greater than the value')
        self.left_child = left_child
        if right_child != None and not right_child.value > self.value:
            raise ValueError
            print('right child must be less or equal than the value')
        self.right_child = right_child
    
    def print_node(self):
        print(' ', self.parent)
        print(' ', '|')
        print(' ', self.value)
        print('/', '', '\\')
        print(self.right_child, '', self.left_child)

class Binary_Search_Tree:
    def __init__(self, value = None, left_child = None, right_child = None):
        self.tree = []
        if value != None:
            self.root = Node(value)
            if left_child != None:
                self.root.left_child = left_child
            if right_child != None:
                self.root.right_child = right_child
            self.tree.append(self.root)

    def search(self, key, node = None, start_from_root = False):
        if node == None and start_from_root:
            node = self.root

        elif node == None:
            return None

        if key == node.value:
            return node

        elif key < node.value:
            return self.search(key, node = node.left_child)

        elif key > node.value:
            return self.search(key, node = node.right_child)

    def insert(self, key, parent_node = None, node == None):
        if node == None:
            return Node(key)

        if key < node.value:
            return self.insert()

if __name__=='__main__':
    sth = Binary_Search_Tree(5, Node(2, 5, Node(1), Node(4)), Node(8, 5, Node(6), Node(9)))
    print(sth.search(6, start_from_root = True).value)