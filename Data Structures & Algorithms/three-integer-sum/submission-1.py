class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Sort nums first so we can use the two pointer approach

        The idea is:
        - fix one number nums[a]
        - then use two pointers, l and r, to find two other numbers that make the total 0

        Once nums is sorted:
        - if nums[a] > 0, we can break
        - this is because nums[a] and every number after it will also be positive
        - so we can no longer make a sum of 0

        We also skip duplicate values of nums[a]
        - if nums[a] is the same as nums[a - 1], we have already processed this starting value
        - skipping it prevents duplicate triplets

        For each fixed nums[a]:
        - l starts just after a
        - r starts at the end of the array
        - calculate nums[a] + nums[l] + nums[r]

        If the sum is too small:
        - move l right to increase the sum

        If the sum is too large:
        - move r left to decrease the sum

        If the sum is exactly 0:
        - add the triplet to the result
        - move both pointers inward
        - skip duplicate l and r values so we do not add the same triplet again

        TC: O(n^2), where n is the length of nums
        - O(n log n) to sort
        - O(n^2) because for each a, the l/r pointers scan the rest of the array
        - O(n^2) dominates O(n log n)

        SC: O(1) extra space, ignoring the output array
        - nums.sort() sorts the input list in-place
        - the two pointer logic only uses a few variables
        '''

        nums.sort()
        res = []

        for a in range(len(nums) - 2):
            if nums[a] > 0:
                break
            
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            
            l, r = a + 1, len(nums) - 1

            while l < r:
                result = nums[a] + nums[l] + nums[r]

                if result < 0:
                    l += 1
                elif result > 0:
                    r -= 1
                else:
                    res.append([nums[a], nums[l], nums[r]])

                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        
        return res