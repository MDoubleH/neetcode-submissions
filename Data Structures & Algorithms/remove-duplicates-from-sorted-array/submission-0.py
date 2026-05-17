class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        l will keep track of non duplicates
        l begins at index 0
        r begins at index 1 

        while r < end of array
        if r == l then we must keep incrementing r till we find a num that doesn't equal l
        then do l+=1 and place the number there. l will also keep track of nums that are unique
                '''
        l,r = 0, 1

        while r < len(nums):
            if nums[l] != nums[r]:
                l+=1
                nums[l], nums[r] = nums[r], nums[l]
            r+=1
        
        return l+1