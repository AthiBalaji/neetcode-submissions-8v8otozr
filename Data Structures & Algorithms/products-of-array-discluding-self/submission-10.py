class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #array of nums
        n = len(nums)
        
        #prefix and suffix arrays 
        prefix = [0 for x in range(n)]
        suffix = [0 for x in range(n)]
        
        #edge case handling: prefix of the first element
        # there is no prefix for the first element
        # we want to be able to 
        prefix[0] = 1
        
        #simultaneous loop iteration 
        for i in range(1, n):
            prefix[i] = prefix[i-1]*nums[i-1]
        
        suffix[n-1] = 1
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1]*nums[i+1]
        result = []
        for i in range(n):
            result.append(prefix[i]*suffix[i])
        return result


        # prefix of each of the element from the array of elements



        

        




        


        


            
        