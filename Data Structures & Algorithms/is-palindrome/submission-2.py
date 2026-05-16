class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        Use two pointers, one starting at the beginning and one starting at the end

        Since a palindrome reads the same forwards and backwards, we can compare
        the left and right valid characters at the same time

        We only care about alphanumeric characters
        - If the left pointer is on a non-alphanumeric character, skip it
        - If the right pointer is on a non-alphanumeric character, skip it

        Once both pointers are on valid characters:
        - compare them in lowercase so the check is case-insensitive
        - if they do not match, return False
        - otherwise move both pointers inward

        If the pointers cross without finding a mismatch, the string is a valid palindrome

        TC: O(n), where n is the length of s
        - Each character is visited at most once by either the left or right pointer

        SC: O(1)
        - We do not build a cleaned version of the string
        - We only use two pointer variables
        '''

        l, r = 0, len(s) - 1

        while l <= r:
            while l <= r and not s[l].isalnum():
                l += 1
            
            while l <= r and not s[r].isalnum():
                r -= 1
            
            if l <= r and s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        
        return True