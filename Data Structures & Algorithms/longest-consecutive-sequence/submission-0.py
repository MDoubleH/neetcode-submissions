class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 0
        res = set(nums)

        for n in res:
            cur_len=1
            while n+1 in res:
                n+=1
                cur_len+=1
            length = max(length,cur_len)
        
        return length