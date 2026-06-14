class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Initialise a count dict:
            key: letter -> value: count
        maxf var
            Holds the current max frequency so we know what the number of the most freq int is and we don't have to keep checking dict
        l to keep track of window
        length to keep track of length

        Go through the string s 
        Add to our count dict, increase its value
        Update our maxf
        while our window - maxf > k aka we need to change more than k letters to have the longest substring of same letters
            decrement count of character at l, if that letter's count is 0 then delete from dict
            increment l 
            recalculate maxf with all dict values
        calc length
        return length
        '''
        count = {}
        maxf = 0
        l = 0
        length = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r-l+1) - maxf > k:
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    del count[s[l]]
                
                l += 1
                maxf = max(count.values())
            
            length = max(length, r-l+1)
        
        return length
