class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        -distance,x,y
        we need to sort by distance but also need to have max heap to get closest to 0
        '''

        self.heap = []
        for x,y in points:
            dist = x**2 + y**2
            print(dist)

            if len(self.heap) < k:
                heapq.heappush(self.heap,(-dist,x,y))
            elif dist < abs(self.heap[0][0]):
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, (-dist,x,y))

        res = []
        for dist,x,y in self.heap:
            res.append([x,y])
        
        return res