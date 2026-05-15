class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        L will keep track of where we want to place elements + how many we have that are non val
        R will scan through array, we skip past vals as we don't want them or need to do anything with them
        Non-vals will need to be swapped at L because we want to keep track of non vals and keep them at the start
        also, increment L to not only keep count but also track of where to store elems
        '''

        l = 0

        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l+=1
        
        return l