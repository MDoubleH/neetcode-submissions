from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Use a hash map where the key represents the character frequency pattern.

        The idea is:
        - anagrams have the same characters with the same counts
        - for each word, build a count array of size 26
        - convert that count array into a tuple so it can be used as a dictionary key
        - group all words with the same frequency pattern together

        This works because words like "eat", "tea", and "ate" will all produce
        the same character count key.

        TC: O(n * m), where n is the number of strings and m is the average string length
        SC: O(n), excluding the output, because we store groups in the hash map
        '''

        # Maps character frequency pattern -> list of words with that pattern.
        anagrams = defaultdict(list)

        for s in strs:
            # chars[i] stores how many times the ith letter appears in this word.
            chars = [0] * 26

            # Build the frequency count for the current word.
            for c in s:
                chars[ord(c) - ord("a")] += 1

            # Convert the list to a tuple because lists cannot be dictionary keys.
            anagrams[tuple(chars)].append(s)
        
        # Return all grouped anagram lists.
        return list(anagrams.values())