class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Find this point of rotation
        Check to see if we are on right side or left side
        If our midpoint is  greater than right side then we are in left sorted portion
        we then check, is our target smaller than leftmost element? if not then we must go right!!
        Else mid is < right side
        Check is target greater than right side? if so, go left

        '''

        l, r = 0, len(nums)-1

        while l<=r:
            mid = l + (r-l) // 2
            if target == nums[mid]:
                return mid
            
            print("mid, ", nums[mid])

            #left sorted portion
            if nums[l] <= nums[mid]:
                #Think logically - if our target is smaller than our smallest val or
                #target > than our mid, then we must go right
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                #if target bigger than our biggest num or smaller than our current num
                #go left
                if target > nums[r] or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return -1
        