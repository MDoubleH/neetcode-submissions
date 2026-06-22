class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        l, r = 1, k

        while l<=r:
            mid = l+(r-l)//2

            time = 0
            for pile in piles:
                time += math.ceil(pile / mid)
            
            if time <= h:
                r = mid - 1
                k = mid
            else:
                l = mid + 1
        
        return k