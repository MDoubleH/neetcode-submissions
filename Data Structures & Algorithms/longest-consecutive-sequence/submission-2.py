class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Keep track of max length
        Convert array nums into a set so we have no duplicates
        Then go through the set nums
        keep track of current length
        If current number is the start of a sequence aka, has no left neighbour
        Increase length by 1 and keep incrementing our current number till we reach no more neighbours
        Then simply take max length to be max between current length and curr max
        return max length

        where n is the length of array nums
        TC: O(n) - 1 pass through the array and set look ups are o(1)
        SC: O(n) - we store the array as a set
        '''

        maxLength = 0
        numSet = set(nums)

        for n in numSet:
            currLen = 1
            if n-1 not in numSet:
                while n+currLen in numSet:
                    currLen+=1

            maxLength = max(currLen, maxLength)
        
        return maxLength
