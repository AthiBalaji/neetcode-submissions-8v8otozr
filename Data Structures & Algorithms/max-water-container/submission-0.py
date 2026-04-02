class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        area = 0
        while(l<r):
            limit = min(heights[l], heights[r])
            breadth = r-l
            area = max(area, limit*breadth)
            if(heights[l]<=heights[r]):
                l+=1
            else:
                r-=1
        return area

        