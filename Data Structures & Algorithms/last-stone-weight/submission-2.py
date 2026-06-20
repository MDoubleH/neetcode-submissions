import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        Use a max heap because each turn needs the two heaviest stones.

        Python's heapq is a min heap, so we store each stone as negative.
        This makes the heaviest stone come out first.

        The idea is:
        - convert stones to negative values
        - heapify the list
        - while there are at least two stones, pop the two heaviest
        - if they are different, push the remaining weight back
        - at the end, return the last stone if one exists, otherwise 0

        TC: O(n log n), where n is the number of stones
        SC: O(1) extra space because we mutate the input list in-place
        '''

        # Convert stones into negative values so heapq behaves like a max heap.
        for i in range(len(stones)):
            stones[i] = -stones[i]

        max_heap = stones
        heapq.heapify(max_heap)

        # Keep smashing stones while we have at least two stones available.
        while len(max_heap) > 1:
            # Pop the two heaviest stones and convert them back to positive weights.
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)

            # If the stones are equal, both are destroyed.
            # If they are different, x is always heavier than y, so push x - y back.
            if x != y:
                heapq.heappush(max_heap, -(x - y))

        # If one stone remains, return its positive weight. Otherwise, return 0.
        return -max_heap[0] if max_heap else 0