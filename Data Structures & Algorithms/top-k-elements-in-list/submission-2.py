class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Bucket sort approach.

        Count the frequency of each number.
        Then place each number into a bucket based on its frequency.
        Since the max possible frequency is len(nums), we create len(nums) + 1 buckets.
        Then scan buckets from highest frequency to lowest and collect k numbers.

        n = len(nums)

        TC: O(n)
        - Count frequencies: O(n)
        - Place unique numbers into buckets: O(n)
        - Scan buckets: O(n)

        SC: O(n)
        - count stores up to n unique numbers
        - freq has n + 1 buckets
        - each unique number is stored once in a bucket
        - res stores up to k numbers
        '''
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        freq = [[] for _ in range(len(nums) + 1)]

        for n, c in count.items():
            freq[c].append(n)
        
        res = []

        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)

                if len(res) == k:
                    return res
        
        return res