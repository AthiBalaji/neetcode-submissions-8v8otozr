class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good =set()

        for elem in triplets:
            if elem[0]>target[0] or elem[1]>target[1] or elem[2] > target[2]:
                continue
            if elem[0] == target[0]:
                good.add(0)
            if elem[1] == target[1]:
                good.add(1)
            if elem[2] == target[2]:
                good.add(2)
        return len(good) == 3


            
        

        
        