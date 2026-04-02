class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        bucket = [[] for i in range(len(nums) + 1 )]
        for num in nums:
            res[num] =  1+res.get(num,0)
        
        for num,freq in res.items():
            bucket[freq].append(num)

        result =[]
        for i in range(len(bucket)-1, 0, -1):
            for c in bucket[i]:
                result.append(c)
                if(len(result) == k):
                    return result