class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        eating_rate = r

        while l <= r:
            mid = l + (r-l) // 2
            curr_time = 0

            for pile in piles:
                curr_time += math.ceil(pile / mid)

            if curr_time <= h:
                r = mid - 1
                eating_rate = min(eating_rate, mid)
            else:
                l = mid + 1

        return eating_rate



