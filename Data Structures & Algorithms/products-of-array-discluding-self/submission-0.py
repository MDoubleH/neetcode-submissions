class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        prod = 1

        for i in range(len(nums)):
            res[i] = res[i] * prod
            prod = prod * nums[i]
        
        prod = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] = res[i] * prod
            prod = prod * nums[i]
        
        return res

