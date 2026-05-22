class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Use a sliding window with a set

        The goal is to find the longest substring with no repeated characters

        seen stores the characters currently inside the window
        l tracks the left side of the window
        r scans through the string from left to right
        length keeps track of the longest valid window found so far

        At each step:
        - if s[r] is already in seen, then the current window has a duplicate
        - keep removing characters from the left side until s[r] can be added safely
        - add s[r] to the window
        - update length using the current valid window size

        This works because the set always represents the current substring
        from l to r with no duplicates

        TC: O(n), where n is the length of s
        - r moves through the string once
        - l also moves through the string at most once
        - set add, remove, and lookup are O(1) average

        SC: O(n)
        - in the worst case, all characters are unique and stored in the set
        '''

        seen = set()
        length = 0
        l = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            length = max(length, r - l + 1)
            
        return length