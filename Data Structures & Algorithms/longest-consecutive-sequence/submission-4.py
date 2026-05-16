class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Need max_len to keep track of the longest sequence found so far

        Convert nums into a set
        - this removes duplicates
        - this also lets us check if a number exists in O(1) average time

        Go through each number in the set
        - If n - 1 exists, then n is not the start of a sequence, so we skip it
        - If n - 1 does not exist, then n must be the start of a sequence

        Once we find the start of a sequence:
        - keep increasing the current length while the next number exists
        - compare the current sequence length with max_len
        - keep whichever is bigger

        This avoids brute forcing from every number
        We only build sequences from their true starting point

        TC: O(n), where n is the length of nums
        - O(n) to convert nums into a set
        - O(n) to go through the set
        - The while loop is still O(n) overall because each sequence is only expanded from its start
        - Set lookups are O(1) average

        SC: O(n)
        - In the worst case, all numbers are unique and stored in the set
        '''

        max_len = 0
        nums_set = set(nums)

        for n in nums_set:
            if n - 1 not in nums_set:
                curr_len = 1

                while n + curr_len in nums_set:
                    curr_len += 1

                max_len = max(curr_len, max_len)
        
        return max_len