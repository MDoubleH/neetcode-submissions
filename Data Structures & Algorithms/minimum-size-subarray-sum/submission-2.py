class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        l = 0
        length = float("inf")

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                length = min(length, r-l+1)
                total -= nums[l]
                l+=1
            
        if length == float("inf"):
            return 0
        else:
            return length