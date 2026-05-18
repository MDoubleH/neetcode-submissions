class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Sort the array,
        nums = [-1,0,1,2,-1,-4]
        nums = [-4, -1, -1, 0, 1, 2]

        3 pointers. We will start with a pointer a from the beginning 
        just a simple for loop to go through nums
        if nums[a] > 0 then just break since we cannot make 0
        if a>0 and nums[a]==nums[a-1] then we must continue because we cannot have duplicates!!
        Then run the basic 2 sum with l,r pointers

        ''' 
        nums = sorted(nums)
        res = []

        for a in range(len(nums)-1):
            if nums[a] > 0:
                break
            
            if a>0 and nums[a]==nums[a-1]:
                continue
            
            l,r = a+1, len(nums)-1
            while l<r:
                result = nums[a]+nums[l]+nums[r]

                if result < 0:
                    l+=1
                elif result > 0:
                    r-=1
                else:
                    res.append([nums[a],nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
        
        return res
                




