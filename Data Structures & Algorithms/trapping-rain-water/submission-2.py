class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        maxL, maxR boundaries 

        If the wall at left is lower, then we move ahead and check if current wall is lower
        - if so, then trapped now adds on this space for water - maxL- height[l] as there is space for water to be trapped here
        - else, update maxL to be the boundary here

        Do the same for the right

        This works because we look to find where the height is tallest but also only move the shorter wall ensuirng we have tallest walls at each end and only adding water in dips of height!
        '''
        
        if not height:
            return 0

        trapped_water = 0

        l, r = 0, len(height)-1
        maxL = height[l]
        maxR = height[r]


        while l < r:
            if maxL <= maxR:
                l+=1
                if height[l] < maxL:
                    trapped_water += maxL-height[l]
                else:
                    maxL = height[l]
            else:
                r-=1
                if height[r] < maxR:
                    trapped_water+=maxR-height[r]
                else:
                    maxR = height[r]
    
        return trapped_water

