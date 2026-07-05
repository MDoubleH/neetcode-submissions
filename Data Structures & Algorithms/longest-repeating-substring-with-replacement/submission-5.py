class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Go through chars
        encounter a new character, add to dict and update maxf with that new char
        if len window > k - len window -> (r-l+1) - maxf >2 
        then we must remove letters from our window and update the dict as well
        Keep track of max length as well
        '''
        count = defaultdict(int)
        maxF = 0
        max_length = 0
        l=0

        for r in range(len(s)):
            curr_window = (r-l+1)
            count[s[r]] = 1 + count.get(s[r],0)
            maxF = max(maxF, count[s[r]])

            if curr_window - maxF > k:
                count[s[l]] -= 1
                l+=1
            
            max_length = max(max_length, r-l+1)
        
        return max_length