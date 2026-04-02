class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashy = dict()
        for i in nums:
            if i in hashy:
                return True
            hashy[i] =1
        return False
        
         