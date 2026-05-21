class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        length = float("inf")
        curr_sum = 0

        for r in range(len(nums)):
            curr_sum += nums[r]

            while curr_sum >= target:
                length = min(length, r-l+1)
                curr_sum -= nums[l]
                l+=1
            
        return 0 if length == float("inf") else length

