class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Use sorting + two pointers.

        The idea is:
        - sort the array first so we can move pointers based on the sum
        - fix one number nums[a]
        - then use two pointers to find two other numbers that make the total 0

        For each fixed nums[a]:
        - if the total is too large, move r left to get a smaller number
        - if the total is too small, move l right to get a larger number
        - if the total is 0, add the triplet and skip duplicates

        This works because sorting gives us control over whether to increase
        or decrease the current sum.

        TC: O(n^2), where n is the length of nums
        SC: O(n), because sorted(nums) creates a new sorted copy
        '''
        res = []
        nums = sorted(nums)

        for a in range(len(nums)):
            # Skip duplicate fixed values so we do not repeat the same triplet.
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            
            # Since the array is sorted, if nums[a] is positive,
            # every number after it is also positive, so we cannot sum to 0.
            if nums[a] > 0:
                continue
            
            # Use two pointers to find the remaining two values.
            l, r = a + 1, len(nums) - 1

            while l < r:
                total = nums[a] + nums[l] + nums[r]

                if total > 0:
                    # Sum is too large, so move right pointer left to reduce it.
                    r -= 1
                elif total < 0:
                    # Sum is too small, so move left pointer right to increase it.
                    l += 1
                else:
                    # Found a valid triplet.
                    res.append([nums[a], nums[l], nums[r]])

                    l += 1
                    r -= 1

                    # Skip duplicate left values to avoid duplicate triplets.
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        
        return res