from heap import Heap
from binary_search_tree import Binary_Search_Tree
from binary_search_tree import Node

def huffman_code(characters, weights):
    # this dictionary is used for finding characters also insert new pair of merged characters
    address = {}
    # to save and hold Nodes and also values
    nodes = []
    values = []
    # for loop to fill address dictionary
    for index in range(len(characters)):
        address[weights[index]] = characters[index]
    # create a heap for minimum calculation
    heap = Heap(weights)
    # repeat step in the while loop until heap length become one
    while heap.length > 1:
        # find two most minimum values
        min_number_one, min_number_two = heap.min(), heap.min()
        # find corresponding characters in address dictionary
        char_number_one, char_number_two = address.get(min_number_one), address.get(min_number_two)
        summed_values = min_number_one + min_number_two
        # merging characters and insert it to address and also heap
        address[summed_values] = ''.join([char_number_one, char_number_two])
        heap.insert(summed_values)
        # create a Node and insert it to tree
        if min_number_one in values:
            for node in nodes:
                if node.value is min_number_one:
                    min_number_one = node
        else:
            values.append(min_number_one)
            min_number_one = Node(value = min_number_one)

        if min_number_two in values:
            for node in nodes:
                if node.value is min_number_two:
                    min_number_two = node
        else:
            values.append(min_number_two)
            min_number_two = Node(value = min_number_two)

        new_node = Node(value = summed_values, left_child = min_number_one, right_child = min_number_two)
        min_number_one.parent, min_number_two.parent = new_node, new_node
        nodes.append(min_number_one)
        nodes.append(min_number_two)
        nodes.append(new_node)
        values.append(summed_values)
    
    # cleaning address from waste items and only keep first generation weights
    number_of_items_must_be_removed = len(address.items()) - len(weights)
    for item in range(number_of_items_must_be_removed):
        address.popitem()

    # this function is return address of a weight
    def node_address(key):
        list_of_binaries = []
        loop_backed_node = None

        for node in nodes:
            if node.value is key:
                loop_backed_node = node
        
        while loop_backed_node.parent is not None:
            parent_node = loop_backed_node.parent
            if parent_node.left_child.value is loop_backed_node.value:
                list_of_binaries.append(0)
            else:
                list_of_binaries.append(1)

            loop_backed_node = loop_backed_node.parent
        
        return list(reversed(list_of_binaries))
        
    list_of_letter_binary_value = []
    for weight in weights:
        value = node_address(key = weight)
        letter = address.get(weight)
        list_of_letter_binary_value.append([letter, value])

    return list_of_letter_binary_value

if __name__=='__main__':
    characters = ['a', 'b', 'c', 'd', 'e', 'f']
    weights = [5, 9, 12, 13, 16, 45]
    print(huffman_code(characters = characters, weights = weights))