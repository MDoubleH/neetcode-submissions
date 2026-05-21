class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total = k*threshold

        running_sum = 0
        res = 0
        l=0

        for r in range(len(arr)):
            running_sum+=arr[r]

            if r-l+1 == k:
                if running_sum >= total:
                    res+=1
                
                running_sum -= arr[l]
                l+=1
            
        return res
            