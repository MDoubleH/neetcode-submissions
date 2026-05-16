class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        Use two pointers because the input array is already sorted

        Start with:
        - left pointer at the smallest number
        - right pointer at the largest number

        At each step, calculate the sum of numbers[l] and numbers[r]

        If the current sum is too small:
        - move the left pointer right
        - this increases the sum because the array is sorted

        If the current sum is too large:
        - move the right pointer left
        - this decreases the sum because the array is sorted

        If the current sum equals the target:
        - return the 1-indexed positions, so return l + 1 and r + 1

        TC: O(n), where n is the length of numbers
        - Each pointer only moves inward, so we scan the array once

        SC: O(1)
        - We only use two pointer variables and no extra data structure
        '''

        l, r = 0, len(numbers) - 1

        while l < r:
            curr_sum = numbers[l] + numbers[r]

            if curr_sum < target:
                l += 1
            elif curr_sum > target:
                r -= 1
            else:
                return [l + 1, r + 1]
        
        return []