class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Resultant array to hold 1s, neutral vals so we can carry out multiplication
        Calculate prefix - multiplication of nums before current position
        curr multiplier needs to be 1 and we have to multiply each number in nums by it to get prefix val
        Go through nums, our current position in resultant array will be curr multiplier * res[i]
        multiplier will be multiplier * current nums

        Then do the same for post fix

        This multiplication will get us to our solution

        '''

        res = [1]*len(nums)

        #prefix
        multiplier = 1
        for i in range(len(nums)):
            res[i] = res[i] * multiplier
            multiplier = multiplier * nums[i]
        
        #postfix
        multiplier = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] = res[i] * multiplier 
            multiplier = multiplier * nums[i]

        return res