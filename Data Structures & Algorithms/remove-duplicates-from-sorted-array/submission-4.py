class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        l = 0

        for r in range(len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l+=1
        
        return l