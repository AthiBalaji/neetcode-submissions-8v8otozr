class Solution:
    def isHappy(self, n: int) -> bool:
        res = n 
        visited = set()

        while res not in visited and res != 1:
            visited.add(res)
            digitsum = 0
            while res != 0:
                digitsum += (res%10)**2 
                res= res//10
            res = digitsum

        return res == 1  


