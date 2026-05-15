class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        1. Go through each item in the array O(n)
        2. Check if the current item, already exists in our set O(1), if so, return True
        3. Add to a set O(1) time 
        4. If we reach the end of the list and have gone through all items O(n), return False

        Time complexity: O(n) where n = nums
        Space comlpexity: O(n) where n = nums
        '''

        seen = set()

        for n in nums:
            if n in seen:
                return True
            else:
                seen.add(n)
        
        return False