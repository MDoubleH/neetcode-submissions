import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        Use a max heap of size k.

        The idea is:
        - we only want to keep the k closest points seen so far
        - Python has a min heap, so we store negative distances to simulate a max heap
        - the furthest point among our current k closest points will be at the top
        - if the heap grows bigger than k, remove that furthest point

        This works because any point removed from the heap is further than the k best points
        we have kept so far, so it cannot be part of the final answer.

        TC: O(n log k), where n is the number of points
        SC: O(k), because the heap stores at most k points
        '''
        max_heap = []

        for x, y in points:
            # We can use squared distance because we only need to compare distances.
            # No need to take square root, since it preserves the same ordering.
            dist = x ** 2 + y ** 2

            # Store negative distance so the largest distance behaves like the smallest heap value.
            heapq.heappush(max_heap, [-dist, x, y])

            # If we have more than k points, remove the furthest one.
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        # Return the points left in the heap. Order does not matter for this problem.
        return [[x, y] for dist, x, y in max_heap]