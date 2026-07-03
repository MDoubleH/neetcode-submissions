class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        Use vertical scanning.

        The idea is:
        - use the first string as the reference prefix
        - check each character index across every string
        - as soon as one string ends or a character does not match,
          we return the prefix built so far

        This works because the longest common prefix must match every string
        character by character from the start.

        TC: O(n * m), where n is the number of strings and m is the length checked
        SC: O(1) auxiliary space, excluding the output string
        '''
        res = ""

        # Go through each character index in the first string.
        for i in range(len(strs[0])):

            # Check whether every string has the same character at this index.
            for s in strs:
                # If this string ends, or the character does not match,
                # the common prefix stops here.
                if i == len(s) or strs[0][i] != s[i]:
                    return res

            # If all strings matched at index i, add this character to the prefix.
            res += strs[0][i]

        return res