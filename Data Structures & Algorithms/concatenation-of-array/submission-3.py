class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        '''
        TC: O(2n) -> O(n)
        SC: O(n)
        '''
        ans = []
        length_of_nums = len(nums)
        for i in range(length_of_nums*2):
            ans.append(nums[i%length_of_nums])
        
        return ans
