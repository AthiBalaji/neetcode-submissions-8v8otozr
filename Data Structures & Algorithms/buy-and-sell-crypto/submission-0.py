class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        lowest = prices[0]
        for i in prices:
            if(i < lowest):
                lowest = i
            temp = i - lowest
            if(temp>best):
                best = temp
        return best
