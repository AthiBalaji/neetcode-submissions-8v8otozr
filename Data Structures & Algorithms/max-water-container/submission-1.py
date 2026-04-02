class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        area = 0 
        while l <r:
            if heights[l]<=heights[r]:
                area = max(area,(r-l)*heights[l])
                l+=1
            elif heights[r]< heights[l]:
                area = max(area,(r-l)*heights[r])
                r-=1

        return area


        