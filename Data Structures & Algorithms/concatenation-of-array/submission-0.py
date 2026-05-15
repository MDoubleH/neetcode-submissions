class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        '''
        1. Create ans array, then Go through the array nums twice - use range(len(nums)*2)
        2. add to the ans array - must use modulo so we can loop back and grab correct index
        modulo = remainder so we get correct position / index
        3. Return array ans

        TC: o(2n) = O(n) where n is the length of nums 
        SC: O(2n) = O(n)
        '''

        ans = []

        for i in range(len(nums)*2):
            ans.append(nums[i%len(nums)])
        
        return ans