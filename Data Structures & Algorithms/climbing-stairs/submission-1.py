class Solution:
    def climbStairs(self, n: int) -> int:
        ways = 1
        lookup = {0:1, 1:1}
        for i in range(2, n+1):
            ways = lookup[i-1]+lookup[i-2]
            lookup[i] = ways
        
        return ways

            
        