class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        o(n) tc
        o(n) sc
        '''
        seen = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        
        return False