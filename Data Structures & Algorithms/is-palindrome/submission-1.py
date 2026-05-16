class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        Initialise left and right pointer
        keep going till left and right pointers cross
        while l<=r
        while l<=r and s[l] char at left pointer is not alphanaumerical then keep iterating left pointer
        Do the same for right pointer but just decrement
        if l<=r s[l].lower and s[r].lower - we need to compare the lower case letters of both
        if they dont match then just return false
        Else we just decrement and increase both at end
        '''

        l,r = 0, len(s)-1

        while l<=r:
            while l<=r and not s[l].isalnum():
                l+=1
            
            while l<=r and not s[r].isalnum():
                r-=1
            
            if l<=r and s[l].lower() != s[r].lower():
                return False
            
            l+=1
            r-=1
        
        return True