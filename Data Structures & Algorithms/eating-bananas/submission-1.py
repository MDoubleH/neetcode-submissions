class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        Our max eating rate can be max of piles, which is what we set our r value to
        We do binary search as it is log(n) and we have a range of vals from 1 to max(piles)
        Do binary search
        Our calculation is that we keep track of time
        We see how long it takes to go through each pile and get it to 0
        If that time is <= h then we can decrease the number of bananas we need to eat per pile aka reduce r
        else increase l as we must eat more bananas in order to finish all piles within allotted time

        binary search because we have a range of vals we can be and quicker to remove half of those numbers wiht bin search

        '''

        l, r = 1, max(piles)
        result = r

        while l <= r:
            bananas_eaten = l + (r-l) // 2

            time = 0

            for pile in piles:
                time += math.ceil(pile/bananas_eaten)
            
            if time <= h:
                result = min(bananas_eaten, result)
                r = bananas_eaten-1
            else:
                l = bananas_eaten+1
        
        return result


