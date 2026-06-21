class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        convert nums to a set - so we don't count duplicates
        keep track of length 
        Go through array nums 
        if n-1 doesn't exist in our array - then we have found the start of our array
        while n+1 is in our array
        Increment length and keep counting 
        Then length = max(length, curr_length)
        return length
        '''

        max_length = 0
        nums_set = set(nums)

        for n in nums_set:
            if n-1 not in nums_set:
                curr_length = 1
                while n+curr_length in nums_set:
                    curr_length += 1
                
                max_length = max(curr_length, max_length)
        
        return max_length
