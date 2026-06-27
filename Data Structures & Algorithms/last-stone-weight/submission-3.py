class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        max heap
        '''
        max_heap = []
        heapq.heapify(max_heap)

        for s in stones:
            heapq.heappush(max_heap, -s)

        while len(max_heap) > 1:
            x, y = -heapq.heappop(max_heap), -heapq.heappop(max_heap)

            if x > y:
                heapq.heappush(max_heap,-(x-y))
        
        if max_heap:
            return -max_heap[0]
        else:
            return 0


