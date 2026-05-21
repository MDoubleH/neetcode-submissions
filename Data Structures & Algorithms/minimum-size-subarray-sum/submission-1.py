class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        Use a sliding window because all numbers are positive

        The goal is to find the smallest subarray where the sum is at least target

        l tracks the left side of the window
        r scans through nums from left to right
        curr_sum keeps track of the current window sum
        length keeps track of the smallest valid window found so far

        At each step:
        - add nums[r] to curr_sum to expand the window
        - while curr_sum is greater than or equal to target, we have a valid window
        - update length with the current window size
        - then remove nums[l] and move l forward to try and shrink the window

        This works because nums contains positive values
        - expanding the window increases the sum
        - shrinking the window decreases the sum
        - so we can safely move the pointers forward without missing a better answer

        If no valid window is found, length will still be infinity, so return 0

        TC: O(n), where n is the length of nums
        - r moves through the array once
        - l also moves through the array at most once
        - so total work is linear

        SC: O(1)
        - we only use a few variables and no extra data structures
        '''

        l = 0
        length = float("inf")
        curr_sum = 0

        for r in range(len(nums)):
            curr_sum += nums[r]

            while curr_sum >= target:
                length = min(length, r - l + 1)
                curr_sum -= nums[l]
                l += 1
            
        return 0 if length == float("inf") else length