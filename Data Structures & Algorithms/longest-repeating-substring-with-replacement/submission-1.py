class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Use a sliding window with a hashmap to count character frequencies

        The goal is to find the longest substring where we can replace at most k
        characters to make the whole substring the same character

        count stores how many times each character appears in the current window
        l tracks the left side of the window
        r scans through s from left to right
        res stores the longest valid window found so far

        For each window:
        - window size = r - l + 1
        - max(count.values()) gives the most frequent character in the window
        - characters_to_replace = window size - most frequent character count

        If characters_to_replace > k:
        - the window is invalid
        - shrink from the left by removing s[l] from the count
        - move l forward

        If the window is valid:
        - update res with the current window size

        TC: O(n), where n is the length of s
        - r scans through the string once
        - l also moves through the string at most once
        - max(count.values()) is O(26), which is O(1), because the input only has uppercase letters

        SC: O(1)
        - the hashmap stores at most 26 uppercase English letters
        '''

        count = {}
        l = 0
        res = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res