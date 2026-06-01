class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        biggest -> smallest = add the current value/symbol
        e.g. vi = 5+1=6
        smallest -> biggest = subtract the current value / symbol
        e.g iv = -1+5=4

        Go through each char
        So long as we still have another symbol ahead of us and we haven't reached end of list
        and that symbol is bigger than our current symbol 
        then subtract our current value/symbol from res

        else
        just add the current symbol / res
        '''
        roman = {"I": 1, "V":5, "X": 10, "L":50, "C":100,
                "D": 500, "M": 1000}
        
        res = 0

        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
            
        return res
            
            




