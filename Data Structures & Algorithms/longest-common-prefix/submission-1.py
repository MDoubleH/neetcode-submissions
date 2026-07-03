class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        #obtain the index we want to go through
        for i in range(len(strs[0])):
            #go through that index for all our strings
            for s in strs:
                #if we reach the end of a str or no longer match, return
                if i == len(s) or strs[0][i] != s[i]:
                    return res
            res += s[i]

        return res

