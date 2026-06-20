class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -1 * stones[i]


        max_heap = stones
        heapq.heapify(max_heap)


        while max_heap:
            if len(max_heap) == 1:
                return -max_heap[0]
            x, y = -heapq.heappop(max_heap), -heapq.heappop(max_heap)

            # if x == y - don't do anything because both stones have been removed anyways
            if x == y:
                continue
            elif x > y:
                x = x - y
            
            heapq.heappush(max_heap, -x)
        
        return 0
