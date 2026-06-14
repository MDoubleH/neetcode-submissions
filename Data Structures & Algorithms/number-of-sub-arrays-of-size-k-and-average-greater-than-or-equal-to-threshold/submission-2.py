class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = k*threshold
        count = 0
        total = 0

        l = 0
        for r in range(len(arr)):
            total += arr[r]

            if r-l+1 == k:
                if total >= target:
                    count+=1
                total -= arr[l]
                l+=1
            
        return count