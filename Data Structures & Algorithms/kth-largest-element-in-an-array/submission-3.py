import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        Use a min heap of size k.

        The idea is:
        - keep the k largest numbers seen so far
        - the smallest value in that heap is the kth largest overall
        - whenever the heap grows bigger than k, remove the smallest value

        This works because any number that gets popped cannot be part of the top k largest values.

        TC: O(n log k), where n is the length of nums
        SC: O(k), because the heap stores at most k elements

        Much better than heapifying then popping because that would be log n to pop
        '''
        min_heap = []
        
        for num in nums:
            # Add the current number as a candidate for the kth largest.
            heapq.heappush(min_heap, num)

            # If we have more than k numbers, remove the smallest one.
            # This leaves only the k largest numbers seen so far.
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        # The smallest number among the k largest numbers is the kth largest.
        return min_heap[0]