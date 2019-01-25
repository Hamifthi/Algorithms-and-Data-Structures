class Node:
    def __init__(self, value, parent = None, left_child = None, right_child = None):
        self.value = value
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child
    
    def print_node(self):
        print(' ', self.parent)
        print(' ', '|')
        print(' ', self.value)
        print('/', '', '\\')
        print(self.right_child, '', self.left_child)

class Binary_Search_Tree:
    def __init__(self, root_value = None, left_child = None, right_child = None):
        if root_value != None:
            self.root = Node(root_value, parent = None)
            if left_child != None:
                self.root.left_child = left_child
            if right_child != None:
                self.root.right_child = right_child

    def search(self, key, node = None, start_from_root = True):
        if start_from_root:
            node = self.root

        if key == node.value:
            return node

        elif key < node.value:
            return self.search(key, node = node.left_child, start_from_root = False) if node.left_child != None else None

        else:
            return self.search(key, node = node.right_child, start_from_root = False) if node.right_child != None else None

    def insert(self, key: int, parent_node: Node = None):
        if parent_node != None:
            if key <= parent_node.value:
                if parent_node.left_child == None:
                    parent_node.left_child = Node(key, parent = parent_node)
                else:
                    self.insert(key, parent_node = parent_node.left_child)
            else:
                if parent_node.right_child == None:
                    parent_node.right_child = Node(key, parent = parent_node)
                else:
                    self.insert(key, parent_node = parent_node.right_child)

        else:
            self.insert(key, parent_node = self.root)
    
    def minimum_maximum_value(self, min = True, start_at = None):
        if start_at == None:
            starter_node = self.root
        elif type(start_at) == Node:
            starter_node = start_at
        else:
            starter_node = self.search(start_at)
        if min:
            while starter_node != None:
                last_node = starter_node
                starter_node = starter_node.left_child
            return last_node
        
        else:
            while starter_node != None:
                last_node = starter_node
                starter_node = starter_node.right_child
            return last_node

    def in_order_traversal(self, node: Node):
        if node == None:
            pass
        else:
            print(node.value)
            self.in_order_traversal(node = node.left_child)
            self.in_order_traversal(node = node.right_child)

        return 'finish'

    def predecessor_successor(self, key):
        node = self.search(key)
        if node.left_child != None:
            predecessor = self.minimum_maximum_value(min = False, start_at = node.left_child)
        else:
            if node.parent.value < node.value:
                predecessor = node.parent
            else:
                predecessor = node.parent.parent
        if node.right_child != None:
            successor = self.minimum_maximum_value(min = False, start_at = node.right_child.left_child)
        else:
            if node.parent.value > node.value:
                successor = node.parent
            else:
                successor = node.parent.parent
        try:
            return predecessor, successor
        except UnboundLocalError:
            return successor
        except UnboundLocalError:
            return successor
        else:
            return None, None
 
    def delete_node(self, key):
        if type(key) == Node:
            node = key
        else:
            node = self.search(key)

        if node.left_child == None and node.right_child == None:
            try:
                if node.value == node.parent.left_child.value:
                    node.parent.left_child = None
            except AttributeError:
                pass
            try:
                if node.value == node.parent.right_child.value:
                    node.parent.right_child = None
            except AttributeError:
                pass
            del node
        
        elif node.left_child == None or node.right_child == None:
            alternative = node.left_child if node.left_child != None else node.right_child
            try:
                if node.value == node.parent.left_child.value:
                    node.parent.left_child = alternative
            except AttributeError:
                pass
            try:
                if node.value == node.parent.right_child.value:
                    node.parent.right_child = alternative
            except AttributeError:
                pass
            del node

        else:
            predecessor = self.predecessor_successor(node.value)[0]
            node.value, predecessor.value = predecessor.value, node.value
            self.delete_node(predecessor)


if __name__=='__main__':
    # sth = Binary_Search_Tree(5, Node(2, 5, Node(1), Node(4)), Node(8, 5, Node(6), Node(9)))
    # print(sth.search(6, start_from_root = True).value)
    sth = Binary_Search_Tree(5)
    sth.insert(2, sth.root)
    sth.insert(8, sth.root)
    sth.insert(1)
    # print(sth.search(3))
    print(sth.minimum_maximum_value(min = False).value)
    # print(sth.in_order_traversal(sth.root))
    print(sth.delete_node(5))
    print(sth.in_order_traversal(sth.root))