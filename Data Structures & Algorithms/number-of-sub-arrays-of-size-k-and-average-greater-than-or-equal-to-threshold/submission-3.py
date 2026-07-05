class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = k*threshold
        curr_total = 0
        l = 0
        res = 0

        for r in range(len(arr)):
            curr_total += arr[r]

            if r-l+1 == k:
                if curr_total >= target:
                    res+=1
                curr_total-=arr[l]
                l+=1
        
        return res