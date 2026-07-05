class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_sub = float("inf")
        curr_total = 0
        l = 0

        for r in range(len(nums)):
            curr_total += nums[r]

            while curr_total >= target:
                min_sub = min(min_sub, r-l+1)
                curr_total -= nums[l]
                l+=1
        
        if min_sub == float("inf"):
            return 0
        else:
            return min_sub