class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0,len(numbers)-1
        while(l<r):
            if(numbers[l]+numbers[r]>target):
                r-=1
            elif(target>numbers[l]+numbers[r]):
                l+=1
            elif(numbers[l]+numbers[r]==target):
                res = [0]*2
                res = [l+1,r+1]
                return res
        return []
                