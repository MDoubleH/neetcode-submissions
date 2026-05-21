class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        Use a sliding window with a set

        The idea is:
        - keep a window of numbers where the index distance is at most k
        - if we ever see the same number again while it is still inside the window,
          then we have found two equal values with distance <= k

        seen stores the numbers currently inside the valid window

        l tracks the left side of the window
        r scans through nums from left to right

        At each index r:
        - if the window size becomes bigger than k, remove nums[l] from seen
          and move l forward
        - then check if nums[r] already exists in seen
        - if it does, that means nums[r] appeared before within distance k,
          so return True
        - otherwise, add nums[r] to seen

        If we finish scanning and never find a nearby duplicate, return False

        TC: O(n), where n is the length of nums
        - r scans through the array once
        - set add, remove, and lookup are O(1) average

        SC: O(k)
        - the set only stores numbers inside the current window of size at most k
        - in the worst case this is O(min(n, k))
        '''

        seen = set()
        l = 0

        for r in range(len(nums)):
            if abs(r - l) > k:
                seen.remove(nums[l])
                l += 1
            
            if nums[r] in seen:
                return True
            
            seen.add(nums[r])
        
        return False