class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Use two pointers / one pass through the prices array

        The idea is:
        - l represents the best day to buy so far
        - r represents the current day we are checking as a possible sell day

        We want to buy low and sell high
        So for each price at r:
        - if prices[r] is greater than prices[l], we can make a profit
        - calculate the profit and update max profit if it is bigger

        If prices[r] is less than or equal to prices[l]:
        - this means we found a better/lower buying price
        - so move l to r

        This works because:
        - we always keep l as the lowest price seen so far
        - and we check the best profit we can make by selling at each future day

        If no profitable trade exists, profit remains 0

        TC: O(n), where n is the length of prices
        - we scan through the prices once

        SC: O(1)
        - we only use a few variables and no extra data structures
        '''

        profit = 0
        l = 0

        for r in range(1, len(prices)):
            if prices[r] > prices[l]:
                profit = max(profit, prices[r] - prices[l])
            else:
                l = r
        
        return profit