class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        Use binary search on the answer.

        The eating speed can be anywhere from:
        - 1 banana per hour
        - max(piles) bananas per hour

        The key idea is that if Koko can finish at some speed k,
        then she can also finish at any faster speed.
        So the search space is monotonic:
        - if speed is fast enough, try a smaller speed
        - if speed is too slow, try a larger speed

        For each possible speed, we calculate how many hours it would take
        to finish all piles. Each pile takes ceil(pile / speed) hours because
        Koko can only eat from one pile per hour.

        TC: O(n log m), where n is the number of piles and m is max(piles)
        SC: O(1), because we only use a few variables
        '''

        l, r = 1, max(piles)
        result = r

        while l <= r:
            # Try the middle eating speed.
            speed = l + (r - l) // 2
            time = 0

            # Calculate how many hours this speed would take.
            for pile in piles:
                time += math.ceil(pile / speed)
            
            if time <= h:
                # This speed works, so save it and try to find an even smaller valid speed.
                result = min(speed, result)
                r = speed - 1
            else:
                # This speed is too slow, so we need to eat more bananas per hour.
                l = speed + 1
        
        return result