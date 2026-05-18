class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        Use two pointers because water trapped at any position depends on the
        tallest wall to its left and the tallest wall to its right

        l starts at the beginning of the array
        r starts at the end of the array

        maxl keeps track of the tallest height seen so far from the left
        maxr keeps track of the tallest height seen so far from the right

        At each step:
        - compare height[l] and height[r]
        - move the pointer with the smaller height

        We move the smaller side because:
        - the amount of water is limited by the shorter boundary
        - if height[l] <= height[r], then the right side is already tall enough
          to act as a boundary, so we can safely process the left side
        - if height[r] < height[l], then the left side is already tall enough
          to act as a boundary, so we can safely process the right side

        When processing a side:
        - if the current height is below the max height seen on that side,
          it can trap water
        - trapped water = side max - current height
        - otherwise, update the side max

        TC: O(n), where n is the length of height
        - each pointer only moves inward, so each index is processed at most once

        SC: O(1)
        - we only use two pointers, two max variables, and the trapped total
        '''
        if not height:
            return 0
            
        trapped = 0

        l, r = 0, len(height) - 1
        maxl = height[l]
        maxr = height[r]

        while l < r:
            if height[l] <= height[r]:
                l += 1

                if height[l] < maxl:
                    trapped += maxl - height[l]
                else:
                    maxl = height[l]
            else:
                r -= 1

                if height[r] < maxr:
                    trapped += maxr - height[r]
                else:
                    maxr = height[r]

        return trapped