class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        Use a sliding window with hash maps.

        The idea is:
        - count the character frequencies in s1
        - move a window of size len(s1) across s2
        - if any window has the same character counts as s1, then that window is a permutation

        This works because permutations have the same characters with the same frequencies,
        just in a different order.

        TC: O(n) if we treat the alphabet size as constant, where n is len(s2)
        SC: O(1) if the alphabet is fixed lowercase English letters
        '''
        if len(s1) > len(s2):
            return False
        
        # Frequency map for s1. This is what every valid window must match.
        count_s1 = {}
        for c in s1:
            count_s1[c] = 1 + count_s1.get(c, 0)
        
        l = 0
        k = len(s1)
        count_s2 = {}

        for r in range(len(s2)):
            # Add the new right character into the current window.
            count_s2[s2[r]] = 1 + count_s2.get(s2[r], 0)

            # Once the window reaches size k, compare it against s1's frequency map.
            if r - l + 1 == k:
                if count_s2 == count_s1:
                    return True

                # Slide the window forward by removing the left character.
                count_s2[s2[l]] -= 1

                # Delete zero-count characters so the dictionary comparison stays accurate.
                if count_s2[s2[l]] == 0:
                    del count_s2[s2[l]]

                l += 1

        return count_s1 == count_s2