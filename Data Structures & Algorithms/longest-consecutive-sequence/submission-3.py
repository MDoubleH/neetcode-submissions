class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        - Need max_len var to keep track of current max length
        Need a set for nums so we don't include duplicates in our max_len or TLE
        Go through nums set, if there exists a number before it then continue
        Else we have found the start of a possible sequence
          - Keep track of this sequence and keep increasing len so long as bigger num exists
          - Compare current length with max length and take which ever is bigger
        return length

        TC:
        O(n) to go through the nums and convert to set 
        O(n) to go through the set of nums (could be all unique initially)
        Overall O(n)

        SC: O(n) as all nums can be unique and stored in set
        '''
        max_len = 0
        nums_set = set(nums)

        for n in nums_set:
            if n-1 not in nums_set:
                curr_len = 1
                while n+curr_len in nums_set:
                    curr_len+=1
                max_len = max(curr_len, max_len)
        
        return max_len