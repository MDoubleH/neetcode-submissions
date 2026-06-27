class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        # heapq.heapify(min_heap)
        
        for x,y in points:
            total = x**2+y**2
            heapq.heappush(max_heap, (-total,x,y))

        while len(max_heap) > k:
            heapq.heappop(max_heap)
        
        res = []
        for total,x,y in max_heap:
            res.append([x,y])
        
        return res