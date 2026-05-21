class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        '''
        Use a fixed-size sliding window of length k

        The problem asks for subarrays of size k where the average is at least threshold

        Instead of calculating average each time:
        - average >= threshold
        - sum / k >= threshold
        - sum >= k * threshold

        So we calculate the required total once as k * threshold

        running_sum keeps track of the sum of the current window
        res keeps track of how many valid subarrays we have found
        l tracks the left side of the window
        r scans through arr from left to right

        At each step:
        - add arr[r] to the running_sum
        - once the window size reaches k, check if running_sum is large enough
        - if it is, increment res
        - then remove arr[l] and move l forward to slide the window

        TC: O(n), where n is the length of arr
        - r scans through the array once
        - each element is added once and removed once

        SC: O(1)
        - we only use a few variables and no extra data structures
        '''

        total = k * threshold

        running_sum = 0
        res = 0
        l = 0

        for r in range(len(arr)):
            running_sum += arr[r]

            if r - l + 1 == k:
                if running_sum >= total:
                    res += 1
                
                running_sum -= arr[l]
                l += 1
            
        return res