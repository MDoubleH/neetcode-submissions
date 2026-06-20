class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for x, y in points:
            dist = x**2 + y**2
            heapq.heappush(max_heap, [-dist, x, y])

            #Soon as we reach more than k elems, remove the furthest point from 0,0
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        return [[x,y] for dist, x, y in max_heap]
