class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        n = number of strings
        m = average/max length of each string

        TC: O(n * m)
        - We loop through every string.
        - For each string, we count its characters, which takes O(m).
        - Creating the 26-length tuple key is O(26), which is O(1).

        SC: O(n)
        - The dictionary stores all strings grouped by anagram key.
        - The char_freq array is O(1) because it always has length 26.
        '''
        anagrams = defaultdict(list)

        for s in strs:
            char_freq = [0] * 26

            for c in s:
                char_freq[ord(c) - ord("a")] += 1
            
            anagrams[tuple(char_freq)].append(s)
        
        return list(anagrams.values())