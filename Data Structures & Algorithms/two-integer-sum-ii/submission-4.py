class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l, r = 0, len(numbers)-1
        res = []
        while l<r:
         sum_nums = numbers[l]+numbers[r]
         if sum_nums == target:
            res.append(l+1)
            res.append(r+1)
            return res
         elif sum_nums > target:
            r-=1 
         else:
            l+=1
         
         