class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0 
        n = len(heights)
        stack = []
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][0] > heights[i]:
                pair = stack.pop()
                start = pair[1]
                currentArea = (i - start)*pair[0]
                maxArea = max(maxArea, currentArea)
            stack.append((heights[i], start))
        
        for elem in stack:
            currentArea = (n - elem[1])* elem[0]
            maxArea = max(maxArea, currentArea)

        return maxArea
                
        