class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        Use two pointers because the array is already sorted

        l keeps track of the next position where a unique value should be placed
        r scans through the array looking for new unique values

        Since the array is sorted:
        - duplicates will be next to each other
        - if nums[r] is different from nums[r - 1], then nums[r] is a new unique value

        When we find a new unique value:
        - place it at nums[l]
        - move l forward

        At the end:
        - nums[0:l] contains the unique values
        - l also represents the number of unique values
        - so we return l

        TC: O(n), where n is the length of nums
        - r scans through the array once

        SC: O(1)
        - We modify nums in-place and only use two pointer variables
        '''

        l = 1

        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        
        return l