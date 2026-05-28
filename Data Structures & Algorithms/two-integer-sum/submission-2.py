class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key = num, val = index
        seen = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in seen:
                return [seen[diff], i]
            else:
                seen[n] = i
        
        