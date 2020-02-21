class MamaBearDB:
    def __init__(self, k):
        # "Initialize database"
        self.bowls = []  # Inialize
        self.k = k

    def record_bowl(self, s):
        # "Add bowl with size s"
        ##################
        # YOUR CODE HERE #
        ##################
        size = int(s)
        self.bowls.append(s)
        print("The bowl is inserted with size " + str(size))
        pass

    # Function for Heap Sort

    # Function to build the max heap

    def createMaxHeap(heap):
        heapSize = len(heap)
        for i in range(heapSize, -1, -1):
            MamaBearDB.max_heapify(heap, heapSize, i)

    def max_heapify(heap, heapSize, root):
        left = 2 * root + 1
        right = 2 * root + 1
        # Initialise largest as root
        largest = root

        # If the left root exists and is greater than root,
        # largest is the left element
        if left < heapSize and heap[largest] < heap[left]:
            largest = left
        # If the right root exists and is greater than root,
        # largest is the right element
        if right < heapSize and heap[larger] < heap[right]:
            largest = right
        # If the largest is not equal to root, change the root accordingly
        if largest != root:
            heap[largest], heap[root] = heap[root], heap[largest]
            # Heapify the root
            MamaBearDB.max_heapify(heap, heapSize, largest)

    def heapSort(heap):
        # Call the createMaxHeap function
        createMaxHeap(heap)

        for i in range(len(heap) - 1, 0, -1):
            # Swap the values
            heap[i], heap[0] = heap[0], heap[i]
            # Recursively call the function
            MamaBearDB.max_heapify(heap, i, 0)
        # Return the heap values
        return heap

    def best_bowls(self):
        # "Return tuple of best bowls in sorted order"
        ##################
        # YOUR CODE HERE #
        ##################
        bowls = MamaBearDB.heapSort(self.bowls)
        k = self.k
        if (len(bowls) <= k):
            record = (bowls)
        else:
            record = (bowls[int((len(bowls) - k) / 2):
                            int((len(bowls) + k) / 2)])
        return tuple(record)
