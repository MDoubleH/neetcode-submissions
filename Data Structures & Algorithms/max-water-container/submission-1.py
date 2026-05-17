class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        Use two pointers because we want to find the widest container first,
        then move inward to try and find a taller height

        l starts at the left side of the array
        r starts at the right side of the array

        The area is calculated as:
        - width = r - l
        - height = min(heights[l], heights[r])
        - area = width * height

        We take the smaller height because the container can only hold water
        up to the shorter line

        At each step:
        - calculate the current area
        - update max_area if this area is bigger
        - move the pointer with the smaller height

        We move the smaller height because:
        - the width is always getting smaller as pointers move inward
        - so the only way to possibly find a bigger area is to find a taller line
        - moving the taller line would not help because the smaller line still limits the water

        TC: O(n), where n is the length of heights
        - Each pointer only moves inward, so we scan the array once

        SC: O(1)
        - We only use pointer variables and max_area
        '''

        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            area = width * height

            max_area = max(max_area, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_area