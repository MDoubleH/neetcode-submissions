class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        TC: O(n)
        SC: O(1)
        '''
        l, r = 0, len(heights)-1
        max_area = (r-l) * min(heights[l], heights[r])
        
        while l<r:
            area = (r-l) * min(heights[l], heights[r])
            max_area = max(area, max_area)

            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        
        return max_area