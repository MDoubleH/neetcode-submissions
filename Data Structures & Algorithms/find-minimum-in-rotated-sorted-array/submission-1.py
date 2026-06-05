class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        Find this point of rotation
        Check to see if we are on right side or left side
        If our midpoint is  greater than right side then we are in left sorted portion
        Therefore, left must go l=mid+1 as we know current mid val is too big and there is a smaller val on right side
        Else mid is < right side
        Therefore, right must go to MID as mid CAN be the smallest number and we want to return what mid ends at

        '''

        l, r = 0, len(nums)-1

        while l<r:
            mid = l + (r-l) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        return nums[r]        