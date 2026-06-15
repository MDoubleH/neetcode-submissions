class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        Use binary search because the array is sorted but rotated.

        The idea is to find the rotation point, which is where the smallest value is.

        We compare nums[mid] with nums[r]:
        - if nums[mid] > nums[r], then mid is in the left sorted portion,
          so the minimum must be to the right
        - otherwise, mid is in the right sorted portion,
          so mid could be the minimum, and we keep it in the search space

        The key invariant is that the minimum is always inside [l, r].

        TC: O(log n), because we remove half the search space each time
        SC: O(1), because we only use pointers
        '''

        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] > nums[r]:
                # mid is in the left sorted portion.
                # Since nums[mid] is bigger than nums[r], the minimum is to the right.
                l = mid + 1
            else:
                # mid could be the minimum, so we keep it by moving r to mid.
                r = mid
        
        # When l == r, both pointers are at the minimum value.
        return nums[r]