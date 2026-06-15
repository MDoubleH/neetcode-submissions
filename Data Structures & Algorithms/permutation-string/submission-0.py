class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        if len(s1) < len(s2) then just return False as not possible

        two dictionaries
        populate both with frequencies 

        compare both hashtables as we go through the window of s2
        '''
        if len(s1) > len(s2):
            return False
        
        count_s1 = {}
        for c in s1:
            count_s1[c] = 1 + count_s1.get(c, 0)
        
        l = 0
        k = len(s1)
        count_s2 = {}

        for r in range(len(s2)):
            # print("s2[l] ", s2[l])
            # print("s2[r] ", s2[r])
            count_s2[s2[r]] = 1 + count_s2.get(s2[r], 0)

            if r-l+1 == k:
                if count_s2 == count_s1:
                    return True
                count_s2[s2[l]] -= 1
                if count_s2[s2[l]] == 0:
                    del count_s2[s2[l]]
                l += 1

        return count_s1 == count_s2



