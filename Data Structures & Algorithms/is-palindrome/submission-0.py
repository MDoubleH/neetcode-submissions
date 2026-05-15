class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        1. Initialise our left and right pointers, l = r, r = len(str)-1
        2. while loop till our left and right crosses over
        3. while l < r and l is not alphanum then keep increasing it
        4. same for right pointer
        5. then check and compare the two, if they're equal then continue else return false immediately

        ''' 

        l, r = 0, len(s)-1

        while l <= r:
            while l <= r and s[l].isalnum() == False:
                l+=1
            
            while l <= r and s[r].isalnum() == False:
                r-=1
            
            if l<=r and s[l].lower() != s[r].lower():
                return False
            
            l+=1
            r-=1
        
        return True