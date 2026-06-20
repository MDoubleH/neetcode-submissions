import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        '''
        Use a min heap of size k.

        The idea is:
        - keep only the k largest numbers seen so far
        - the smallest number inside this heap is the kth largest overall
        - if the heap grows bigger than k, remove the smallest value

        This works because anything smaller than the k largest values does not matter
        for finding the kth largest.

        TC for __init__: O(n log n), or O(n log k) if explained by trimming to size k
        TC for add: O(log k)
        SC: O(k), because the heap stores at most k elements
        '''
        self.k = k

        # Start with all the initial numbers.
        self.min_heap = nums 

        # Turn nums into a valid min heap.
        heapq.heapify(self.min_heap)

        # Keep removing the smallest values until only the k largest remain.
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)
        

    def add(self, val: int) -> int:
        # Add the new value into the heap.
        heapq.heappush(self.min_heap, val)

        # If we now have more than k values, remove the smallest one.
        # This keeps only the k largest values seen so far.
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        # The smallest value among the k largest values is the kth largest.
        return self.min_heap[0]