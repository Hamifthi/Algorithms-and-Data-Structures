class Heap:
    def __init__(self, list_of_elements = None):
        if list_of_elements == None:
            self.heap = []
        else:
            self.heap = self.heapify(list_of_elements)
            self.length = len(self.heap)

    def heapify(self, elements):
        while True:
            old_elements = tuple(elements)
            for i in range(int(len(elements) / 2)):
                if elements[i] > elements[2 * i + 1]:
                    elements[i], elements[2 * i + 1] = elements[2 * i + 1], elements[i]
                if elements[i] > elements[2 * i + 2]:
                    elements[i], elements[2 * i + 2] = elements[2 * i + 2], elements[i]
            if elements == list(old_elements):
                break

        return elements

    def bubble_up(self):
        child = self.length - 1
        parent = int(child / 2)
        while self.heap[parent] > self.heap[child] and parent >= 0:
            self.heap[child], self.heap[parent] = self.heap[parent], self.heap[child]
            child = parent
            parent = int(parent / 2) - 1 if parent % 2 == 0 else int(parent / 2)

    def insert(self, element):
        self.heap.append(element)
        self.length += 1
        self.bubble_up()
    
    def bubble_down(self):
        parent = 0
        child = self.heap[parent * 2 + 1] if self.heap[parent * 2 + 1] < self.heap[parent * 2 + 2] else self.heap[parent * 2 + 2]
        while self.heap[parent] > self.heap[child]:
            self.heap[child], self.heap[parent] = self.heap[parent], self.heap[child]
            parent = child
            try:
                child = self.heap[parent * 2 + 1] if self.heap[parent * 2 + 1] < self.heap[parent * 2 + 2] else self.heap[parent * 2 + 2]
            except IndexError:
                pass

    def min(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        min = self.heap.pop()
        self.length -= 1
        self.bubble_down()
        return min

if __name__=='__main__':
    example = [4, 4, 8, 9, 4, 12, 9, 11, 13]

    example = Heap(example)
    print(example.heap)
    example.insert(1)
    print(example.heap)
    print(example.min())
    print(example.heap)