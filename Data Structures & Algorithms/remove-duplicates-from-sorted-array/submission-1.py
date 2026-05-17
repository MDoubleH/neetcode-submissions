class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        Use two pointers because the array is already sorted

        l keeps track of the position of the last unique value we have placed
        r scans through the rest of the array looking for new unique values

        Since the array is sorted:
        - duplicates will be next to each other
        - if nums[r] is different from nums[l], then nums[r] must be a new unique value

        When we find a new unique value:
        - move l forward
        - place nums[r] at nums[l]

        At the end:
        - nums[0:l+1] contains the unique values
        - l is the index of the last unique value
        - so the number of unique values is l + 1

        TC: O(n), where n is the length of nums
        - r scans through the array once

        SC: O(1)
        - We modify nums in-place and only use two pointer variables
        '''

        l = 0
        r = 1

        while r < len(nums):
            if nums[r] != nums[l]:
                l += 1
                nums[l] = nums[r]
            r+=1
        
        return l + 1