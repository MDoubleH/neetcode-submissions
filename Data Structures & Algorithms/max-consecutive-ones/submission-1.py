class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        '''
        1. initialise a max_ones var to keep track of the max; curr_count to keep track of curr number of 1s
        2. loop over the array, if we are at a 1 then our curr_count is increased by 1
        3. else, reach a 0, set max_ones to be the max between current max value and the curr count of 1s, then also reset curr count to 0
        4. return max_ones

        TC: O(n) - where n is length of nums (we need to do a single pass)
        SC: O(1) - we are not defining any new data structures. only constants

        '''

        max_ones = 0
        curr_count = 0

        for n in nums:
            if n == 1:
                curr_count+=1
            else:
                max_ones = max(max_ones, curr_count)
                curr_count = 0
        
        return max(max_ones, curr_count)

