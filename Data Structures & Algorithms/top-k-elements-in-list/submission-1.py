class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Use a frequency map + bucket sort.

        The idea is:
        - first count how many times each number appears
        - then place each number into a bucket based on its frequency
        - index i in freq stores all numbers that appear i times
        - then scan the buckets from highest frequency to lowest frequency

        This works because the maximum possible frequency is len(nums),
        so we can directly map each count to a bucket instead of sorting.

        TC: O(n), where n is the length of nums
        SC: O(n), because we store the frequency map and bucket array
        '''

        # Count how often each number appears.
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # freq[i] will store all numbers that appear exactly i times.
        # We need len(nums) + 1 buckets because a number can appear up to len(nums) times.
        freq = [[] for i in range(len(nums) + 1)]

        # Put each number into the bucket matching its frequency.
        for n, c in count.items():
            freq[c].append(n)
        
        res = []

        # Go from highest frequency to lowest frequency.
        # As soon as we collect k numbers, we can return.
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)

                if len(res) == k:
                    return res
        
        return res