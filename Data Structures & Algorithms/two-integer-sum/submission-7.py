class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        tc: o(n)
        sc: o(n)
        '''

        seen = {}

        for i, n in enumerate(nums):
            difference = target - n

            if difference in seen:
                return [seen[difference], i]
            
            seen[n] = i
        
