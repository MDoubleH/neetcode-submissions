class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        Check to see which part of rotated array we are in 
        if mid > r then we simply go to l = mid + 1
        else r = mid

        at beginning we can check if nums[l] < mid then just do lowest = min between that and mid?

        '''

        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r-l) // 2


            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        return nums[r]