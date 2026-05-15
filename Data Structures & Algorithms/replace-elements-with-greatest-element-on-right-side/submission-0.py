class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        '''
        right max value tracked - set at -1 initially
        Reverse through the array
        compute a new max between current value and right most value
          - must be a new var as we do not want to overwrite our current val with just itself
        Set current val to maxRight val
        Set maxRight val to new val 
        '''

        rightMax = -1

        for r in range(len(arr)-1, -1, -1):
            newMax = max(rightMax, arr[r])
            arr[r] = rightMax
            rightMax = newMax
        
        return arr