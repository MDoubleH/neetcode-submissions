class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        nums_set = set(nums)

        for n in nums_set:
            if n-1 not in nums_set:
                curr_len=1
                while n + curr_len in nums_set:
                    curr_len += 1
            
                max_len = max(curr_len, max_len)
        
        return max_len
