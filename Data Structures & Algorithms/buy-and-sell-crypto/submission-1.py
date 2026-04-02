class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        res = 0
        for elem in prices:
            lowest = min(elem, lowest)
            res = max(res, elem-lowest)
        return res

        