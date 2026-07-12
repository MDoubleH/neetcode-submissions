class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.heap = []

        for n in nums:
            if len(self.heap) < k:
                heapq.heappush(self.heap, n)
            elif n > self.heap[0]:
                heapq.heapreplace(self.heap,n)
        
        return self.heap[0]

