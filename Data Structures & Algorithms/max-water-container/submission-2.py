class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0 
        l,r = 0, len(heights)-1
        
        while l<r:
            if heights[l] < heights[r]:
                g = l 
            else:
                g = r 
            print("l r g", l, r,g)
            print("maxArea", maxArea, (r-l)*heights[g])
            maxArea = max(maxArea,(r-l)*heights[g])
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return maxArea


        