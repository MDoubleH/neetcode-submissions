class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Use a sliding window with a hashmap to count character frequencies

        The goal is to find the longest substring where we can replace at most k
        characters to make the whole substring the same character

        count stores character frequencies inside the current window
        max_freq stores the highest frequency of any character we have seen in the window
        l tracks the left side of the window
        r scans through s from left to right
        res stores the longest valid window found so far

        For each window:
        - window size = r - l + 1
        - max_freq is the count of the most common character
        - window size - max_freq tells us how many characters need replacing

        If window size - max_freq > k:
        - we need too many replacements
        - so the window is invalid
        - shrink the window from the left

        If the window is valid:
        - update res with the current window size

        TC: O(n), where n is the length of s
        - r scans through the string once
        - l also moves through the string at most once

        SC: O(1)
        - the hashmap stores at most 26 uppercase English letters
        '''

        count = {}
        l = 0
        res = 0
        max_freq = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            max_freq = max(max_freq, count[s[r]])

            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res