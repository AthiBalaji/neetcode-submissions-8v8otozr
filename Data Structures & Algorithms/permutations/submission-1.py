class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        temp =[[]]
        for i, x in enumerate(nums):        
            if i != 0:
                temp = newtemp
            newtemp= []
            for p in temp:
                for i in range(len(p)+1):
                    pcopy = p.copy()
                    pcopy.insert(i, x)
                    newtemp.append(pcopy)
        return newtemp

            
        