class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Use modified binary search because the array is sorted but rotated.

        The idea is:
        - at every step, one half of the array must still be sorted
        - check whether the left half or right half is sorted
        - then decide whether the target could exist inside that sorted half

        If the target is inside the sorted half, search there.
        Otherwise, search the other half.

        TC: O(log n), because we remove half the search space each time
        SC: O(1), because we only use pointers
        '''

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            # If mid is the target, we can return immediately.
            if target == nums[mid]:
                return mid

            # If nums[l] <= nums[mid], the left half is sorted.
            if nums[l] <= nums[mid]:
                # If target is outside the sorted left half,
                # then it must be on the right side.
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    # Otherwise, target is inside the sorted left half.
                    r = mid - 1

            # Otherwise, the right half must be sorted.
            else:
                # If target is outside the sorted right half,
                # then it must be on the left side.
                if target > nums[r] or target < nums[mid]:
                    r = mid - 1
                else:
                    # Otherwise, target is inside the sorted right half.
                    l = mid + 1
        
        return -1