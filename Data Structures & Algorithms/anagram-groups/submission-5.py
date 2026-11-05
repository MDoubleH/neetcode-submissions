class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        anagrams = defaultdict(list)

        '''
        Create dict to hold key val pairs
            - key will be the chars and freq
            - value will be the word in the strings list 
        Must obtain position of each characters in an array to act as our key
        '''

        for s in strs:
            chars = [0] * 26
            for c in s:
                chars[ord(c) - ord("a")] += 1
            
            anagrams[tuple(chars)].append(s)

        return list(anagrams.values())

