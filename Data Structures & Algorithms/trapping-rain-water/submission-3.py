class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        maxL = height[l]
        maxR = height[r]
        water = 0

        while l < r:
            if height[l] < height[r]:
                l+=1
                curr_height = height[l]
                if curr_height < maxL:
                    water += maxL - curr_height
                else:
                    maxL = curr_height
            else:
                r -= 1
                curr_height = height[r]
                if curr_height < maxR:
                    water += maxR - curr_height
                else:
                    maxR = curr_height
        
        return water

