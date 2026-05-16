class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Create a result array filled with 1s because 1 is the neutral value for multiplication

        The idea is to store the product of everything before and after each index without using division

        First pass: calculate prefix products
        - multiplier keeps track of the product of all values before the current index
        - store that multiplier in res[i]
        - then update multiplier by multiplying it with nums[i]

        Second pass: calculate postfix products
        - reset multiplier back to 1
        - go through nums from right to left
        - multiplier now represents the product of all values after the current index
        - multiply res[i] by this postfix multiplier
        - then update multiplier by multiplying it with nums[i]

        By the end:
        - res[i] contains prefix product * postfix product
        - which gives product of all elements except nums[i]

        TC: O(n), where n is the length of nums
        - O(n) for the prefix pass
        - O(n) for the postfix pass
        - O(2n) simplifies to O(n)

        SC: O(1) extra space
        - We only use the multiplier variable
        - The result array is required for the output, so we do not count it as extra space
        - If counting the output array, space would be O(n)
        '''

        res = [1] * len(nums)

        # Prefix pass: store product of all values before each index
        multiplier = 1
        for i in range(len(nums)):
            res[i] = res[i] * multiplier
            multiplier = multiplier * nums[i]
        
        # Postfix pass: multiply by product of all values after each index
        multiplier = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * multiplier 
            multiplier = multiplier * nums[i]

        return res